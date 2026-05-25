# Python 学习记录

这是我的 Python 学习记录仓库，用来保存从基础语法到小项目实践过程中的代码、示例和练习内容。

仓库按照学习阶段进行目录划分，每个目录对应一个主题，便于后续复习、整理和继续扩展。

## 目录结构

```text
Python/
├─ 01_VariableLogic/      # 变量、条件判断、逻辑运算
├─ 02_LoopControl/        # for 循环、while 循环
├─ 03_BaseType/           # 列表、字典、元组、集合等基础数据类型
├─ 04_Function/           # 函数、lambda、解包、推导式、作用域
├─ 05_File/               # 文件读写、异常处理、CSV、JSON、配置和日志
├─ 06_OllamaChat/         # 基于 Ollama 和 Streamlit 的 AI 聊天助手练习
└─ main.py                # 根目录示例入口
```

## 学习内容

### 01_VariableLogic

主要记录 Python 基础语法中的变量、简单案例和逻辑运算。

包含内容：

- 变量定义与使用
- 条件判断
- 逻辑运算
- 基础练习案例

### 02_LoopControl

主要记录循环控制相关内容。

包含内容：

- `for` 循环
- `while` 循环
- 循环中的基础控制逻辑

### 03_BaseType

主要记录 Python 常见基础数据类型的使用。

包含内容：

- `list` 列表
- `dict` 字典
- `tuple` 元组
- `set` 集合
- 基础数据类型练习

### 04_Function

主要记录函数相关知识点。

包含内容：

- 函数定义与调用
- lambda 表达式
- 变量作用域
- 序列解包
- 推导式

### 05_File

主要记录文件操作和常见数据格式处理。

包含内容：

- 文本文件读取与写入
- 文件指针操作
- 异常处理
- CSV 文件处理
- JSON 文件处理
- 配置文件管理
- 简单日志系统

### 06_OllamaChat

这是一个 AI 聊天助手练习项目，主要用于学习 Streamlit 页面开发，以及通过 Ollama 调用本地大模型。

包含内容：

- Streamlit 前端页面
- 聊天消息展示
- 会话状态管理
- Ollama 接口调用封装
- 图标和页面组件练习

## 运行方式

本仓库中的大部分文件都是独立的 Python 练习脚本，可以直接在 PyCharm 中运行对应的 `.py` 文件。

也可以在命令行中进入项目目录后运行：

```bash
python main.py
```

运行某个具体练习文件，例如：

```bash
python 03_BaseType/List.py
```

如果运行 `06_OllamaChat` 中的 Streamlit 项目，需要先安装依赖：

```bash
pip install streamlit requests
```

然后运行：

```bash
streamlit run 06_OllamaChat/FrontendSimplify.py
```

如果使用 Ollama 聊天功能，需要本地已经安装并启动 Ollama 服务。

## 仓库说明

这个仓库主要用于个人学习记录，因此目录会随着学习进度持续更新。

建议提交到 GitHub 时忽略以下内容：

- `.idea/`
- `__pycache__/`
- `*.pyc`
- 日志文件
- 本地临时文件

## 后续计划

- 补充每个阶段的学习笔记
- 整理代码注释和示例说明
- 为较完整的小项目单独补充 README
- 持续增加 Python 进阶内容和项目实践
