"""
	模块:单个的py文件,包含Python代码,可以被导入使用
	包:包含__init__.py文件,可以包含多个模块和子包
	init.py的作用
		1.标记当前目录为包:有init.py的目录识别为包,否则不是包
		2.初始化包
		3.定义公共接口

"""

"""
完整的包结构
	myproject/
	├── README.md
	├── setup.py
	├── requirements.txt
	├── mypackage/
	│   ├── __init__.py
	│   ├── core/
	│   │   ├── __init__.py
	│   │   ├── engine.py
	│   │   └── utils.py
	│   ├── io/
	│   │   ├── __init__.py
	│   │   ├── reader.py
	│   │   └── writer.py
	│   └── config.py
	├── tests/
	│   ├── __init__.py
	│   └── test_core.py
	└── examples/
		└── example.py
"""