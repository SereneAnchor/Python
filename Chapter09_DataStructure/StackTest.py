from Stack import Stack

def runTest():
	#创建栈,栈中无任何元素
	stack=Stack()
	print(f"栈为空:{stack.isEmpty()}")

	#元素进栈
	stack.pushItem('A')
	stack.pushItem('B')
	stack.pushItem('C')
	stack.printStack()

	print(f"获取栈顶:{stack.peekItem()}")
	print(f"移除栈顶:{stack.popItem()}")

	stack.printStack()
	print(f"栈长度:{stack.getLength()}")

if __name__=="__main__":
	runTest()