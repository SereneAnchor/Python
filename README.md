# Python 学习记录

[中文](#python-学习记录) | [English](#english-version)

这是我的 Python 学习记录仓库，用来保存从基础语法、面向对象、文件操作，到数据结构和小项目实践过程中的代码、示例和测试内容。

仓库按照学习阶段进行目录划分，每个目录对应一个主题，便于后续复习、整理和继续扩展。

## 目录结构

```text
Python/
├─ Chapter01_VariableControl/    # 变量、条件判断、逻辑控制
├─ Chapter02_LoopControl/        # for 循环、while 循环
├─ Chapter03_BaseType/           # 列表、字典、元组、集合、字符串等基础类型
├─ Chapter04_Function/           # 函数、lambda、解包、推导式、作用域
├─ Chapter05_File/               # 文件读写、异常处理、CSV、JSON、配置和日志
├─ Chapter06_OllamaChat/         # 基于 Ollama 和 Streamlit 的 AI 聊天助手练习
├─ Chapter07_Object/             # 面向对象编程：类、对象、封装、继承、多态等
├─ Chapter08_Advanced/           # 闭包、装饰器和多进程等进阶内容
└─ Chapter09_DataStructure/      # 数据结构实现与测试
```

## 学习内容

### Chapter01_VariableControl

主要记录 Python 基础语法中的变量、条件判断和逻辑控制。

### Chapter02_LoopControl

主要记录循环控制相关内容，包括 `for` 循环、`while` 循环和基础循环逻辑。

### Chapter03_BaseType

主要记录 Python 常见基础数据类型的使用，包括列表、字典、元组、集合和字符串等内容。

### Chapter04_Function

主要记录函数相关知识点，包括函数定义、lambda 表达式、变量作用域、序列解包和推导式。

### Chapter05_File

主要记录文件操作和常见数据格式处理。

包含内容：

- 文本文件读取与写入
- 文件指针操作
- 异常处理
- CSV 文件处理
- JSON 文件处理
- 配置文件管理
- 简单日志系统

### Chapter06_OllamaChat

这是一个 AI 聊天助手练习项目，主要用于学习 Streamlit 页面开发，以及通过 Ollama 调用本地大模型。

包含内容：

- Streamlit 前端页面
- 聊天消息展示
- 会话状态管理
- Ollama 接口调用封装
- 页面组件练习

### Chapter07_Object

主要记录 Python 面向对象编程相关内容。

包含内容：

- 类与对象
- 封装
- 继承
- 方法重写
- 多态
- 抽象类和抽象方法
- 魔法方法
- 单例模式
- 类方法和静态方法

### Chapter08_Advanced

主要记录 Python 进阶语法和并发基础。

包含内容：

- 闭包、自由变量和 `nonlocal`
- 基础装饰器和装饰器语法糖
- 带参数装饰器和多个装饰器
- `functools.wraps` 和函数信息保留
- 耗时统计、异常捕获和日志装饰器
- 多进程基础和自定义进程类

### Chapter09_DataStructure

主要记录常见数据结构的手写实现和对应测试。

当前包含内容：

- 线性结构：顺序表、栈、队列
- 链式结构：单链表、双链表、链栈、链队
- 哈希：哈希表
- 堆：最大堆、最小堆
- 树：二叉树、二叉搜索树
- 并查集
- 图：基础图、有向图、加权图
- 缓存：LRU 缓存

## 运行方式

本仓库中的大部分文件都是独立的 Python 练习脚本，可以直接在 PyCharm 中运行对应的 `.py` 文件。

也可以在命令行中进入项目目录，运行某个具体练习文件，例如：

```bash
python Chapter03_BaseType/01_List.py
```

运行数据结构测试文件，例如：

```bash
python Chapter09_DataStructure/03_Hash/01_HashTableTest.py
```

如果运行 `Chapter06_OllamaChat` 中的 Streamlit 项目，需要先安装依赖：

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
- 暂未整理的 `AAA/`、`Chapter10_/` 和 `Chapter11_/`

## 后续计划

- 继续完善图结构、遍历算法和测试
- 完善部分数据结构的测试文件
- 整理代码注释和示例说明
- 持续增加 Python 进阶内容和项目实践

---

# English Version

[中文](#python-学习记录) | [English](#english-version)

This repository records my Python learning journey, including code examples, practice scripts, data structure implementations, tests, and small projects.

The repository is organized by learning stages. Each folder focuses on one topic so that the learning path is easy to review, maintain, and extend.

## Project Structure

```text
Python/
├─ Chapter01_VariableControl/    # Variables, conditions, and logic control
├─ Chapter02_LoopControl/        # for loops and while loops
├─ Chapter03_BaseType/           # Lists, dictionaries, tuples, sets, strings, and basic types
├─ Chapter04_Function/           # Functions, lambda, unpacking, comprehensions, and scope
├─ Chapter05_File/               # File I/O, exceptions, CSV, JSON, config, and logging
├─ Chapter06_OllamaChat/         # AI chatbot practice with Ollama and Streamlit
├─ Chapter07_Object/             # Object-oriented programming
├─ Chapter08_Advanced/           # Closures, decorators, multiprocessing, and advanced topics
└─ Chapter09_DataStructure/      # Data structure implementations and tests
```

## Learning Topics

### Chapter01_VariableControl

This section covers Python variables, conditions, and basic logic control.

### Chapter02_LoopControl

This section covers loop control, including `for` loops, `while` loops, and basic loop logic.

### Chapter03_BaseType

This section covers common Python data types, including lists, dictionaries, tuples, sets, and strings.

### Chapter04_Function

This section covers function-related topics, including function definitions, lambda expressions, variable scope, sequence unpacking, and comprehensions.

### Chapter05_File

This section covers file operations and common data formats.

Main topics:

- Text file reading and writing
- File pointer operations
- Exception handling
- CSV processing
- JSON processing
- Config file management
- Simple logging system

### Chapter06_OllamaChat

This is an AI chatbot practice project. It is mainly used to learn Streamlit page development and how to call a local large language model through Ollama.

Main topics:

- Streamlit frontend pages
- Chat message display
- Session state management
- Ollama API wrapper
- Page component practice

### Chapter07_Object

This section covers Python object-oriented programming.

Main topics:

- Classes and objects
- Encapsulation
- Inheritance
- Method overriding
- Polymorphism
- Abstract classes and abstract methods
- Magic methods
- Singleton pattern
- Class methods and static methods

### Chapter08_Advanced

This section covers advanced Python syntax and multiprocessing basics.

Main topics:

- Closures, free variables, and `nonlocal`
- Basic decorators and decorator syntax
- Parameterized decorators and stacked decorators
- `functools.wraps` and function metadata preservation
- Timing, exception handling, and logging decorators
- Multiprocessing basics and custom process classes

### Chapter09_DataStructure

This section records handwritten implementations and tests for common data structures.

Current topics:

- Linear structures: sequence list, stack, queue
- Linked structures: singly linked list, doubly linked list, linked stack, linked queue
- Hash: hash table
- Heap: max heap, min heap
- Tree: binary tree, binary search tree
- Union find
- Graph: basic graph, directed graph, weighted graph
- Cache: LRU cache

## How to Run

Most files in this repository are independent Python practice scripts. You can run the corresponding `.py` file directly in PyCharm.

You can also enter the project directory and run a specific practice file from the command line:

```bash
python Chapter03_BaseType/01_List.py
```

Run a data structure test file:

```bash
python Chapter09_DataStructure/03_Hash/01_HashTableTest.py
```

To run the Streamlit project in `Chapter06_OllamaChat`, install the dependencies first:

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
- Unfinished `AAA/`, `Chapter10_/`, and `Chapter11_/` directories

## Future Plans

- Continue improving graph structures, traversal algorithms, and tests
- Improve tests for some data structures
- Improve comments and example descriptions
- Continue adding advanced Python topics and project practice
