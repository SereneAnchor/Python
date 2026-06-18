# Python 学习记录

[中文](#python-学习记录) | [English](#english-version)

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
├─ 07_Object/             # 面向对象编程：类、对象、封装、继承、多态等
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

### 07_Object

主要记录 Python 面向对象编程相关内容。

包含内容：

- 类与对象
- 构造方法
- 实例属性和实例方法
- 类属性和类方法
- 静态方法
- 封装
- 继承
- 方法重写
- 多态
- 面向对象练习案例

## 运行方式

本仓库中的大部分文件都是独立的 Python 练习脚本，可以直接在 PyCharm 中运行对应的 `.py` 文件。

也可以在命令行中进入项目目录后运行：

```bash
python main.py
```

运行某个具体练习文件，例如：

```bash
python Chapter03_BaseType/SequenceList.py
```

如果运行 `06_OllamaChat` 中的 Streamlit 项目，需要先安装依赖：

```bash
pip install streamlit requests
```

然后运行：

```bash
streamlit run Chapter06_OllamaChat/FrontendSimplify.py
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

---

# English Version

[中文](#python-学习记录) | [English](#english-version)

This repository records my Python learning journey, including code examples, practice scripts, and small projects from basic syntax to practical development.

The repository is organized by learning stages. Each folder focuses on one topic so that the learning path is easy to review, maintain, and extend.

## Project Structure

```text
Python/
├─ 01_VariableLogic/      # Variables, conditions, and logical operations
├─ 02_LoopControl/        # for loops and while loops
├─ 03_BaseType/           # Lists, dictionaries, tuples, sets, and basic data types
├─ 04_Function/           # Functions, lambda, unpacking, comprehensions, and scope
├─ 05_File/               # File I/O, exceptions, CSV, JSON, config, and logging
├─ 06_OllamaChat/         # AI chatbot practice with Ollama and Streamlit
├─ 07_Object/             # Object-oriented programming: classes, objects, inheritance, polymorphism
└─ main.py                # Root demo entry
```

## Learning Topics

### 01_VariableLogic

This section covers Python variables, simple cases, conditions, and logical operations.

### 02_LoopControl

This section covers loop control, including `for` loops and `while` loops.

### 03_BaseType

This section covers common Python data types, including `list`, `dict`, `tuple`, and `set`.

### 04_Function

This section covers function-related topics, including function definitions, lambda expressions, variable scope, sequence unpacking, and comprehensions.

### 05_File

This section covers file operations and common data formats.

Main topics:

- Text file reading and writing
- File pointer operations
- Exception handling
- CSV processing
- JSON processing
- Config file management
- Simple logging system

### 06_OllamaChat

This is an AI chatbot practice project. It is mainly used to learn Streamlit page development and how to call a local large language model through Ollama.

Main topics:

- Streamlit frontend pages
- Chat message display
- Session state management
- Ollama API wrapper
- Icons and page component practice

### 07_Object

This section covers Python object-oriented programming.

Main topics:

- Classes and objects
- Constructors
- Instance attributes and instance methods
- Class attributes and class methods
- Static methods
- Encapsulation
- Inheritance
- Method overriding
- Polymorphism
- Object-oriented practice cases

## How to Run

Most files in this repository are independent Python practice scripts. You can run the corresponding `.py` file directly in PyCharm.

You can also run scripts from the command line:

```bash
python main.py
```

Run a specific practice file:

```bash
python Chapter03_BaseType/SequenceList.py
```

To run the Streamlit project in `06_OllamaChat`, install the dependencies first:

```bash
pip install streamlit requests
```

Then run:

```bash
streamlit run Chapter06_OllamaChat/FrontendSimplify.py
```

If you use the Ollama chat feature, Ollama should be installed and running locally.

## Repository Notes

This repository is mainly used for personal learning records and will continue to grow as I learn more Python topics.

Recommended files to ignore when pushing to GitHub:

- `.idea/`
- `__pycache__/`
- `*.pyc`
- Log files
- Local temporary files

## Future Plans

- Add notes for each learning stage
- Improve comments and example descriptions
- Add separate README files for larger practice projects
- Continue adding advanced Python topics and project practice
