import customtkinter as ctk
from tkinter import filedialog, messagebox
import subprocess
import os
import threading
import tempfile
import shutil
from pathlib import Path
import re

# 设置界面外观和颜色主题
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class OllamaManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Ollama 本地模型管理器")
        self.geometry("800x650") # 增加了高度以容纳进度条

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --- 顶部操作区 ---
        self.top_frame = ctk.CTkFrame(self, height=50)
        self.top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.top_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.refresh_button = ctk.CTkButton(self.top_frame, text="刷新列表", command=self.refresh_models_list)
        self.refresh_button.grid(row=0, column=0, padx=5, pady=10)

        self.import_button = ctk.CTkButton(self.top_frame, text="导入 GGUF 模型", command=self.import_gguf_model)
        self.import_button.grid(row=0, column=1, padx=5, pady=10)

        self.delete_button = ctk.CTkButton(self.top_frame, text="删除选中模型", command=self.delete_selected_models, fg_color="red", hover_color="darkred")
        self.delete_button.grid(row=0, column=2, padx=5, pady=10)

        # --- 模型列表区 ---
        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="本地模型列表")
        self.scrollable_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")
        self.model_widgets = []

        # --- 进度与状态区 ---
        self.status_frame = ctk.CTkFrame(self, height=60)
        self.status_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        self.status_frame.grid_columnconfigure(0, weight=1)

        self.status_label = ctk.CTkLabel(self.status_frame, text="准备就绪", anchor="w")
        self.status_label.grid(row=0, column=0, padx=10, pady=(5, 0), sticky="ew")

        self.progress_bar = ctk.CTkProgressBar(self.status_frame)
        self.progress_bar.set(0)
        # 初始时隐藏进度条
        self.progress_bar.grid_remove()

        # --- 初始化检查 ---
        self.check_ollama_installed()

    def run_command(self, command):
        """在后台运行shell命令并返回结果"""
        try:
            startupinfo = None
            if os.name == 'nt':
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True,
                encoding='utf-8',
                startupinfo=startupinfo
            )
            return result.stdout, None
        except FileNotFoundError:
            return None, f"错误：命令 '{command[0]}' 未找到。请确保 Ollama 已安装并已添加到系统 PATH。"
        except subprocess.CalledProcessError as e:
            return None, f"命令执行失败: {e.stderr.strip()}"
        except Exception as e:
            return None, f"发生未知错误: {e}"

    def check_ollama_installed(self):
        """检查Ollama是否安装"""
        self.update_status("正在检测 Ollama 环境...")
        if not shutil.which("ollama"):
            messagebox.showerror("错误", "未检测到 'ollama' 命令。\n\n请确认您已正确安装 Ollama，并将其添加到了系统的环境变量(PATH)中。")
            self.update_status("错误：Ollama 未安装或未在 PATH 中。")
            self.disable_buttons()
        else:
            self.update_status("Ollama 环境正常，正在加载模型列表...")
            self.refresh_models_list()

    def disable_buttons(self):
        """禁用所有操作按钮"""
        self.refresh_button.configure(state="disabled")
        self.import_button.configure(state="disabled")
        self.delete_button.configure(state="disabled")
        
    def enable_buttons(self):
        """启用所有操作按钮"""
        self.refresh_button.configure(state="normal")
        self.import_button.configure(state="normal")
        self.delete_button.configure(state="normal")

    def update_status(self, message, progress=None):
        """更新状态栏信息和进度条"""
        self.status_label.configure(text=message)
        if progress is not None:
            # 如果有进度值，显示并更新进度条
            self.progress_bar.grid()
            self.progress_bar.set(progress)
        else:
            # 如果没有进度值，隐藏进度条
            self.progress_bar.grid_remove()
        self.update_idletasks()

    def refresh_models_list(self):
        """刷新并显示本地模型列表"""
        self.update_status("正在刷新模型列表...")
        
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.model_widgets = []

        threading.Thread(target=self._load_models_thread, daemon=True).start()

    def _parse_legacy_ollama_list(self, text_output):
        """解析旧版本ollama list的文本表格输出"""
        models = []
        lines = text_output.strip().split('\n')
        if len(lines) < 2:
            return []

        header = lines[0]
        name_pos = header.find("NAME")
        id_pos = header.find("ID")
        size_pos = header.find("SIZE")
        modified_pos = header.find("MODIFIED")

        if -1 in [name_pos, id_pos, size_pos, modified_pos]:
            return []

        for line in lines[1:]:
            try:
                name = line[name_pos:id_pos].strip()
                size = line[size_pos:modified_pos].strip()
                modified = line[modified_pos:].strip()
                
                if name:
                    models.append({
                        'name': name,
                        'size_str': size,
                        'modified_str': modified
                    })
            except Exception:
                continue
        return models

    def _load_models_thread(self):
        """在后台线程中加载模型"""
        output, error = self.run_command(["ollama", "list"])

        if error:
            if "could not connect to ollama" in error.lower():
                 error_msg = f"无法连接到 Ollama 服务。\n请确认 Ollama 应用程序正在后台运行。\n\n({error})"
            else:
                 error_msg = f"无法获取模型列表:\n{error}\n\n请确认 Ollama 服务正在运行。"
            
            self.after(0, lambda: messagebox.showerror("加载失败", error_msg))
            self.after(0, self.update_status, f"加载失败: {error}")
            return

        models = self._parse_legacy_ollama_list(output)
        self.after(0, self._populate_models_ui, models)

    def _populate_models_ui(self, models):
        """用获取到的模型数据填充UI"""
        if not models:
            no_model_label = ctk.CTkLabel(self.scrollable_frame, text="未找到任何本地模型", text_color="gray")
            no_model_label.pack(pady=20)
            self.update_status("未找到本地模型。")
            return

        for model in models:
            frame = ctk.CTkFrame(self.scrollable_frame)
            frame.pack(fill="x", padx=5, pady=5)
            frame.grid_columnconfigure(1, weight=1)

            checkbox = ctk.CTkCheckBox(frame, text=model['name'])
            checkbox.grid(row=0, column=0, padx=10, pady=10)
            
            info_text = f"大小: {model['size_str']}  |  修改时间: {model['modified_str']}"
            info_label = ctk.CTkLabel(frame, text=info_text, anchor="e", text_color="gray")
            info_label.grid(row=0, column=1, padx=10, pady=10, sticky="e")

            self.model_widgets.append((checkbox, model['name']))
        
        self.update_status(f"加载完成，共找到 {len(models)} 个模型。")

    def delete_selected_models(self):
        """删除所有选中的模型"""
        selected_models = [name for checkbox, name in self.model_widgets if checkbox.get() == 1]
        
        if not selected_models:
            messagebox.showinfo("提示", "请先勾选需要删除的模型。")
            return

        confirm = messagebox.askyesno("确认删除", f"您确定要删除以下 {len(selected_models)} 个模型吗？\n\n- " + "\n- ".join(selected_models) + "\n\n此操作不可恢复！")
        
        if confirm:
            self.disable_buttons()
            threading.Thread(target=self._delete_models_thread, args=(selected_models,), daemon=True).start()

    def _delete_models_thread(self, models_to_delete):
        """在后台线程中执行删除操作并更新进度条"""
        total = len(models_to_delete)
        errors = []
        for i, model_name in enumerate(models_to_delete):
            progress = (i + 1) / total
            self.after(0, self.update_status, f"正在删除 ({i+1}/{total}): {model_name}...", progress)
            _, error = self.run_command(["ollama", "rm", model_name])
            if error:
                errors.append(f"删除 '{model_name}' 失败: {error}")
        
        self.after(0, self.update_status, "删除操作完成，正在刷新列表...")
        
        if errors:
            self.after(0, lambda: messagebox.showerror("删除出错", "\n".join(errors)))

        self.after(0, self.refresh_models_list)
        self.after(0, self.enable_buttons)

    def import_gguf_model(self):
        """处理导入GGUF文件的流程"""
        filepath = filedialog.askopenfilename(
            title="请选择一个 GGUF 模型文件",
            filetypes=[("GGUF files", "*.gguf")]
        )
        if not filepath:
            return

        base_name = Path(filepath).stem.lower().replace('_', '-').replace('.', '-')
        suggested_name = f"{base_name}:latest"

        # 【修复】使用新的方式创建对话框并获取输入
        dialog = ctk.CTkInputDialog(
            text=f"请为新模型命名 (例如: my-model:tag):\nGGUF 文件: {Path(filepath).name}",
            title="命名新模型"
        )
        # CTkInputDialog的get_input()会显示对话框并返回输入值
        new_model_name = dialog.get_input()

        if new_model_name:
            self.disable_buttons()
            threading.Thread(target=self._import_thread, args=(filepath, new_model_name), daemon=True).start()

    def _import_thread(self, gguf_path, model_name):
        """在后台线程中执行导入操作并更新进度条"""
        temp_filepath = None
        try:
            # 步骤1: 创建Modelfile
            self.after(0, self.update_status, f"步骤 1/3: 正在创建临时 Modelfile...", 0.1)
            modelfile_content = f'FROM "{gguf_path}"'
            
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".modelfile", encoding='utf-8') as temp_file:
                temp_file.write(modelfile_content)
                temp_filepath = temp_file.name
            
            self.after(0, self.update_status, f"步骤 2/3: 正在调用 Ollama 创建模型 '{model_name}'...", 0.3)
            self.after(0, lambda: self.progress_bar.configure(mode='indeterminate')) # 设置为不确定模式
            self.after(0, lambda: self.progress_bar.start())

            # 步骤2: 执行ollama create命令
            command = ["ollama", "create", model_name, "-f", temp_filepath]
            _, error = self.run_command(command)

            self.after(0, lambda: self.progress_bar.stop())
            self.after(0, lambda: self.progress_bar.configure(mode='determinate'))

            if error:
                self.after(0, lambda e=error: messagebox.showerror("导入失败", f"创建模型时出错:\n{e}"))
                self.after(0, self.update_status, "导入失败。")
            else:
                self.after(0, self.update_status, f"步骤 3/3: 模型 '{model_name}' 导入成功！正在刷新列表...", 1.0)
                self.after(0, lambda: messagebox.showinfo("成功", f"模型 '{model_name}' 已成功导入！"))
                self.after(0, self.refresh_models_list)

        except Exception as e:
            self.after(0, lambda err=e: messagebox.showerror("导入异常", f"导入过程中发生意外错误:\n{err}"))
            self.after(0, self.update_status, "导入过程中发生异常。")
        finally:
            # 步骤3: 清理临时文件和重置UI
            if temp_filepath and os.path.exists(temp_filepath):
                os.remove(temp_filepath)
            
            self.after(0, self.enable_buttons)
            # 延迟一小段时间后重置状态栏
            self.after(2000, lambda: self.update_status("准备就绪"))

if __name__ == "__main__":
    app = OllamaManagerApp()
    app.mainloop()
