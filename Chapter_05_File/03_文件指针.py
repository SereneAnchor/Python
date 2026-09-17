#文件指针(Example文件内部14个字符)
with open('Example.txt','r',encoding='utf-8') as file:
	#返回当前文件指针的位置
	print(f"指针起始位置:{file.tell()}")

	#从当前文件指针位置开始,读取10个字符
	content=file.read(10)
	print(f"读取十个字符:{content}")

	#查看当前文件指针位置
	print(f"当前指针位置:{file.tell()}")

	#把文件指针移动到文件开头
	file.seek(0)
	print(f"指针移到开头:{file.tell()}")

	#从文件开头开始(0表示文件开头、1表示当前位置、2表示文件末尾),把指针移动到第5个位置
	file.seek(5,0)
	print(f"指针偏移距离:{file.tell()}")

	#从文件末尾开始,指针偏移0个位置
	file.seek(0,2)
	fileSize=file.tell()
	print(f"当前指针位置:{fileSize}")
