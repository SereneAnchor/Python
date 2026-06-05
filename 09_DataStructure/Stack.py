#栈

class Stack:
	#使用列表来存储栈元素
	def __init__(self):
		self.items=[]

	#元素进栈
	def pushItem(self,value):
		self.items.append(value)

	#元素出栈(不返回出栈元素)
	def popItem(self):
		if self.isEmpty():
			print(f"栈空.")
		return self.items.pop()

	#获取栈顶元素
	def peekItem(self):
		if self.isEmpty():
			print(f"栈空.")
		return self.items[-1]

	#获取栈长度
	def getLength(self):
		return len(self.items)

	#判断栈是否为空
	def isEmpty(self):
		return len(self.items)==0

	#输出栈
	def printStack(self):
		print(f"输出栈:{self.items}")


if __name__=="__main__":
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



