# 🚀 Ollama Model Manager - 你的本地 AI 模型管家 🚀

![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.8+-brightgreen.svg)
![UI Framework](https://img.shields.io/badge/UI-CustomTkinter-orange.svg)
![GitHub Repo](https://img.shields.io/badge/GitHub-lzA6/ollama--model--manager-lightgrey?logo=github)

> 👋 你好，未来的 AI 探索者！
>
> 你是否曾为管理本地一堆 Ollama 模型而烦恼？删除模型要敲命令，导入 GGUF 文件要写 `Modelfile`... 这一切是不是有点繁琐，让你感觉自己像个"命令行苦工"？
>
> **我们相信，工具的意义在于解放生产力，让你专注于真正重要的事情——创造与探索，而不是在琐碎的操作上浪费生命。**
>
> Ollama Model Manager 诞生于这样一个纯粹的哲学：**让每一个人，无论你是不是技术专家，都能优雅、轻松地驾驭本地 AI 模型。** 它不仅仅是一个软件，更是一种态度的体现：技术应当是温暖的、亲切的，是连接你与未来科技的桥梁，而不是一堵冷冰冰的墙。

---

## ✨ 核心功能一览

<div align="center">

| 功能 | 描述 | 状态 |
|------|------|------|
| 🎯 **自动环境检测** | 智能检测 Ollama 安装状态和版本 | ✅ 已实现 |
| 📊 **模型可视化列表** | 清晰展示模型名称、大小、修改日期 | ✅ 已实现 |
| 🗑️ **一键批量删除** | 多选模型，批量删除，告别繁琐命令 | ✅ 已实现 |
| 📥 **GGUF 自动导入** | 拖拽 GGUF 文件，自动创建 Modelfile | ✅ 已实现 |
| 🎨 **现代化界面** | 基于 CustomTkinter，支持亮色/暗色主题 | ✅ 已实现 |
| ⚡ **异步操作** | 后台执行耗时任务，界面流畅不卡顿 | ✅ 已实现 |
| 🖥️ **跨平台支持** | Windows、macOS、Linux 全平台兼容 | ✅ 已实现 |

</div>

---

## 🎨 软件界面预览

*(实际运行截图展示)*

```
┌─────────────────────────────────────────────────────────────┐
│  Ollama Model Manager  🚀                                  🗕 🗗 ⓧ │
├─────────────────────────────────────────────────────────────┤
│  🏠 仪表盘    📦 模型管理    ⚙️ 设置                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🔍 本地模型列表 (共 8 个模型)                                │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ ✅ llama3.1:8b-instruct-q4_0      │ 4.2 GB │ 2天前  │    │
│  │ ✅ codellama:7b-instruct-q4_0     │ 3.8 GB │ 1周前  │    │
│  │ ⬜ mistral:7b-instruct-v0.2-q4_0  │ 4.1 GB │ 3天前  │    │
│  │ ⬜ phi3:mini-128k-instruct-q4_0   │ 2.3 GB │ 1天前  │    │
│  │ ⬜ gemma:2b-it-q4_0               │ 1.6 GB │ 5天前  │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  [🗑️ 删除选中模型]  [📥 导入 GGUF 文件]  [🔄 刷新列表]        │
│                                                             │
│  📥 导入新模型                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 📁 选择 GGUF 文件: [浏览...]                         │    │
│  │                                                       │    │
│  │ 🔤 模型名称: [___________________________]           │    │
│  │                                                       │    │
│  │ [开始导入]          [取消]                            │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  📊 系统状态: ✅ Ollama 服务运行正常 | 💾 磁盘使用: 24.3/128 GB │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 这个工具适合谁？

<div align="center">

| 用户类型 | 核心需求 | 解决方案 |
|----------|----------|----------|
| **🤖 AI 应用爱好者** | 频繁尝试新模型，简化导入流程 | 拖拽式 GGUF 导入 |
| **🧹 模型整理控** | 管理大量本地模型，保持整洁 | 可视化批量管理 |
| **⌨️ 命令行恐惧者** | 避免复杂命令，图形化操作 | 直观的 GUI 界面 |
| **🐍 Python 学习者** | 学习 GUI 开发实践案例 | 开源可修改代码 |
| **👨‍💻 效率追求者** | 节省时间，专注核心工作 | 自动化工作流 |

</div>

---

## 🛠️ 安装与使用教程

### 系统要求

| 组件 | 最低要求 | 推荐配置 |
|------|----------|----------|
| **操作系统** | Windows 10 / macOS 10.14+ / Ubuntu 18.04+ | 最新版本 |
| **Python** | 3.8+ | 3.10+ |
| **Ollama** | 0.1.0+ | 最新版本 |
| **内存** | 4 GB | 8 GB+ |
| **存储** | 1 GB 可用空间 | 10 GB+ 可用空间 |

### 第 1 步：环境准备

1. **安装 Python**
   ```bash
   # 检查是否已安装
   python --version
   # 或
   python3 --version
   ```
   - 如果未安装，请访问 [Python 官网](https://www.python.org/downloads/) 下载安装
   - **重要**: 安装时勾选 "Add Python to PATH"

2. **安装 Ollama**
   ```bash
   # 检查是否已安装
   ollama --version
   ```
   - 如果未安装，请访问 [Ollama 官网](https://ollama.com/) 下载安装

### 第 2 步：安装依赖

```bash
# 安装核心依赖
pip install customtkinter

# 或者使用 requirements.txt (如果提供)
pip install -r requirements.txt
```

### 第 3 步：下载与运行

**方法一：直接运行（推荐开发者）**
```bash
# 克隆或下载项目
git clone https://github.com/lzA6/ollama-model-manager.git
cd ollama-model-manager

# 运行程序
python ollama_manager.py
```

**方法二：一键启动脚本**

- **Windows** (`start.bat`):
  ```batch
  @echo off
  chcp 65001 >nul
  echo 正在启动 Ollama Model Manager...
  python ollama_manager.py
  pause
  ```

- **macOS/Linux** (`start.sh`):
  ```bash
  #!/bin/bash
  echo "🚀 启动 Ollama Model Manager..."
  cd "$(dirname "$0")"
  python3 ollama_manager.py
  ```

**方法三：打包版本（未来计划）**
- 下载预编译的可执行文件，无需安装 Python
- 双击即可运行

---

## 🏗️ 系统架构设计

### 整体架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                    Ollama Model Manager                         │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │    🎨 界面层    │  │   🧠 逻辑层     │  │   ⚙️ 执行层     │  │
│  │                 │  │                 │  │                 │  │
│  │ • CustomTkinter │  │ • 业务逻辑      │  │ • subprocess    │  │
│  │ • 主题管理      │  │ • 数据验证      │  │ • 文件操作      │  │
│  │ • 事件处理      │  │ • 状态管理      │  │ • 临时文件      │  │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘  │
│           │                    │                    │           │
│           └────────────────────┼────────────────────┘           │
│                                │                                │
│                        ┌───────▼────────┐                       │
│                        │   🧵 线程管理   │                       │
│                        │                │                       │
│                        │ • 异步任务     │                       │
│                        │ • 进度更新     │                       │
│                        │ • UI 响应      │                       │
│                        └────────────────┘                       │
├─────────────────────────────────────────────────────────────────┤
│                         Ollama 运行时                           │
│  ┌───────────────┐  ┌───────────────┐  ┌─────────────────────┐  │
│  │   模型管理     │  │   模型推理     │  │     文件系统        │  │
│  │               │  │               │  │                     │  │
│  │ • ollama list │  │ • ollama run  │  │ • GGUF 文件         │  │
│  │ • ollama rm   │  │ • ollama pull │  │ • Modelfile         │  │
│  │ • ollama create│ │ • ollama serve│  │ • 模型缓存          │  │
│  └───────────────┘  └───────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 核心模块详解

#### 🎨 界面层 (Presentation Layer)
```python
class ModelManagerUI:
    ├── 主题管理 (ThemeManager)
    │   ├── 亮色/暗色模式切换
    │   └── 自定义颜色方案
    ├── 组件管理 (WidgetManager)  
    │   ├── 模型列表表格
    │   ├── 进度指示器
    │   ├── 对话框管理器
    │   └── 状态栏组件
    └── 事件分发 (EventDispatcher)
        ├── 按钮点击处理
        ├── 文件拖拽支持
        └── 键盘快捷键
```

#### 🧠 逻辑层 (Business Logic Layer)
```python
class ModelManager:
    ├── 模型管理 (ModelManagerCore)
    │   ├── 模型列表获取
    │   ├── 模型信息解析
    │   ├── 批量删除逻辑
    │   └── 状态同步机制
    ├── 导入服务 (ImportService)
    │   ├── GGUF 文件验证
    │   ├── 自动 Modelfile 生成
    │   ├── 导入进度跟踪
    │   └── 错误恢复处理
    └── 配置管理 (ConfigManager)
        ├── 用户偏好设置
        ├── 历史记录管理
        └── 环境配置检测
```

#### ⚙️ 执行层 (Execution Layer)
```python
class OllamaExecutor:
    ├── 命令执行器 (CommandExecutor)
    │   ├── 子进程管理
    │   ├── 输出捕获
    │   ├── 错误处理
    │   └── 超时控制
    ├── 文件处理器 (FileProcessor)
    │   ├── 临时文件管理
    │   ├── 路径解析
    │   ├── 权限检查
    │   └── 清理机制
    └── 兼容性适配器 (CompatibilityAdapter)
        ├── 版本检测
        ├── 特性回退
        └── 格式转换
```

### 数据流示意图

```
用户操作
    │
    ▼
┌─────────────────┐
│   UI 事件触发   │
└─────────────────┘
    │
    ▼
┌─────────────────┐
│  逻辑层业务处理  │
└─────────────────┘
    │
    ▼
┌─────────────────┐
│  异步任务分发   │
└─────────────────┘
    │
    ▼
┌─────────────────┐    ┌─────────────────┐
│  执行层命令调用  │───▶│  Ollama 服务    │
└─────────────────┘    └─────────────────┘
    │                         │
    ▼                         ▼
┌─────────────────┐    ┌─────────────────┐
│  进度状态更新   │    │  结果数据返回   │
└─────────────────┘    └─────────────────┘
    │                         │
    └─────────┬───────────────┘
              ▼
      ┌─────────────────┐
      │   UI 状态刷新   │
      └─────────────────┘
```

---

## 🔧 技术实现深度解析

### 核心技术栈

| 技术组件 | 版本 | 用途 | 优势 |
|----------|------|------|------|
| **Python** | 3.8+ | 核心编程语言 | 简洁易学，生态丰富 |
| **CustomTkinter** | 5.2+ | 现代化 GUI 框架 | 美观界面，暗色主题 |
| **subprocess** | 标准库 | 执行系统命令 | 进程管理，输出捕获 |
| **threading** | 标准库 | 异步任务处理 | 界面响应，并行执行 |
| **tempfile** | 标准库 | 临时文件管理 | 自动清理，安全可靠 |
| **re/json** | 标准库 | 数据解析处理 | 格式转换，兼容适配 |

### 关键技术创新

#### 1. 🧵 智能异步任务系统
```python
class AsyncTaskManager:
    """异步任务管理器 - 确保界面流畅响应的核心"""
    
    def execute_async(self, task_func, callback=None):
        # 创建后台线程执行耗时任务
        thread = threading.Thread(target=self._run_task, 
                                args=(task_func, callback))
        thread.daemon = True
        thread.start()
    
    def _run_task(self, task_func, callback):
        try:
            result = task_func()
            # 通过 after() 方法安全更新 UI
            self.root.after(0, lambda: callback(True, result))
        except Exception as e:
            self.root.after(0, lambda: callback(False, str(e)))
```

#### 2. 🔄 跨版本兼容性引擎
```python
class CompatibilityEngine:
    """兼容性引擎 - 支持不同 Ollama 版本"""
    
    def detect_ollama_version(self):
        """检测 Ollama 版本并启用相应特性"""
        version_output = subprocess.run(
            ["ollama", "--version"], 
            capture_output=True, 
            text=True
        )
        return self._parse_version(version_output.stdout)
    
    def get_models_adaptively(self):
        """自适应获取模型列表"""
        if self.supports_json_output():
            return self._get_models_via_json()
        else:
            return self._get_models_via_legacy()
```

#### 3. 📁 GGUF 智能导入管道
```python
class GGUFImportPipeline:
    """GGUF 文件导入管道 - 完全自动化流程"""
    
    def import_gguf_automatically(self, gguf_path, model_name):
        # 1. 验证文件完整性
        if not self._validate_gguf_file(gguf_path):
            raise ValueError("无效的 GGUF 文件")
        
        # 2. 自动生成 Modelfile
        modelfile_content = f"FROM {gguf_path}"
        temp_modelfile = self._create_temp_modelfile(modelfile_content)
        
        # 3. 执行创建命令
        result = subprocess.run([
            "ollama", "create", model_name, "-f", temp_modelfile
        ], capture_output=True, text=True)
        
        # 4. 清理临时文件
        self._cleanup_temp_files()
        
        return result.returncode == 0
```

### 性能优化策略

#### 内存管理
- **懒加载机制**: 只在需要时加载模型详细信息
- **缓存策略**: 缓存模型列表，减少重复调用
- **及时清理**: 自动清理临时文件和资源

#### 响应性保障
- **任务队列**: 串行化耗时操作，避免资源竞争
- **进度反馈**: 实时更新进度条和状态信息
- **错误边界**: 隔离异常，防止界面崩溃

---

## 📊 优势分析与改进规划

### 核心优势矩阵

<div align="center">

| 维度 | 优势表现 | 用户价值 |
|------|----------|----------|
| **🎯 易用性** | 图形化操作，零命令行 | 降低使用门槛 |
| **⚡ 效率** | 批量操作，自动化流程 | 节省时间成本 |
| **🔧 稳定性** | 完善的错误处理机制 | 可靠的使用体验 |
| **🎨 美观性** | 现代化界面设计 | 愉悦的交互感受 |
| **📚 学习性** | 清晰代码结构 | 优秀的学习案例 |

</div>

### 技术债务与改进方向

| 类别 | 当前状态 | 改进方案 | 优先级 |
|------|----------|----------|--------|
| **错误处理** | 基础异常捕获 | 细化错误类型，提供修复建议 | 🔴 高 |
| **测试覆盖** | 手动测试 | 单元测试 + 集成测试框架 | 🔴 高 |
| **打包分发** | 源码运行 | PyInstaller 打包成可执行文件 | 🟡 中 |
| **性能监控** | 基础日志 | 性能指标收集和分析 | 🟢 低 |
| **文档完善** | 基础 README | 详细用户手册 + API 文档 | 🟡 中 |

---

## 🗺️ 未来发展蓝图

### 短期目标 (v1.1 - v1.3)
- [ ] **一键打包分发**
  - PyInstaller 打包支持
  - 自动更新机制
- [ ] **增强错误处理**
  - 详细的错误诊断
  - 自动修复建议
- [ ] **基础设置面板**
  - Ollama 服务配置
  - 主题个性化设置

### 中期规划 (v1.4 - v2.0)
- [ ] **模型市场集成**
  - Hugging Face 模型浏览
  - 一键下载安装
- [ ] **高级管理功能**
  - 模型备份恢复
  - 磁盘空间管理
- [ ] **性能监控**
  - 模型使用统计
  - 资源占用监控

### 长期愿景 (v2.0+)
- [ ] **插件生态系统**
  - 扩展插件架构
  - 社区插件市场
- [ ] **云同步功能**
  - 配置云端同步
  - 跨设备模型管理
- [ ] **AI 增强功能**
  - 智能模型推荐
  - 自动优化建议

---

## 🤝 贡献指南

我们坚信：**每一个伟大的项目，都源于社区的共同创造。**

### 如何参与贡献

#### 1. 🐛 报告问题
- 使用 Issue 模板提交 Bug 报告
- 提供详细的重现步骤和环境信息

#### 2. 💡 提出建议
- 分享你的使用场景和需求
- 参与功能设计的讨论

#### 3. 🔧 代码贡献
```bash
# 1. Fork 项目
git clone https://github.com/lzA6/ollama-model-manager.git

# 2. 创建功能分支
git checkout -b feature/your-amazing-feature

# 3. 提交更改
git commit -m "feat: add your amazing feature"

# 4. 推送到分支
git push origin feature/your-amazing-feature

# 5. 创建 Pull Request
```

#### 4. 📚 文档改进
- 完善使用文档
- 添加代码注释
- 翻译多语言文档

### 开发环境设置

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 安装开发依赖
pip install -r requirements-dev.txt

# 安装预提交钩子
pre-commit install
```

### 代码规范

- 遵循 PEP 8 编码规范
- 使用类型注解提高代码可读性
- 编写详细的文档字符串
- 确保新增代码包含测试用例

---

## 📄 许可证

本项目采用 **Apache 2.0 许可证** - 详见 [LICENSE](LICENSE) 文件。

### 许可摘要
- ✅ 允许商业使用
- ✅ 允许修改和分发
- ✅ 允许专利使用
- ✅ 提供明确版权声明即可
- ❌ 不提供任何担保

---

## 🌟 致谢

感谢所有为这个项目做出贡献的开发者们！特别感谢：

- **Ollama 团队** - 提供了优秀的本地 AI 模型运行环境
- **CustomTkinter 社区** - 创造了美观易用的 GUI 框架
- **所有测试用户** - 你们的反馈让这个工具越来越好

---

<div align="center">

## 🚀 立即开始你的 AI 模型管理之旅！

[![下载最新版本](https://img.shields.io/badge/下载-最新版本-blue?style=for-the-badge)](https://github.com/lzA6/ollama-model-manager/releases)
[![报告问题](https://img.shields.io/badge/报告-问题-red?style=for-the-badge)](https://github.com/lzA6/ollama-model-manager/issues)
[![参与贡献](https://img.shields.io/badge/参与-贡献-green?style=for-the-badge)](https://github.com/lzA6/ollama-model-manager/pulls)

**让技术回归简单，让创造更加自由**

</div>
