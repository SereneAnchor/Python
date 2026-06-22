#链式栈

class Node:
	#节点中的value保存数据,next指向下一个节点
	def __init__(self,value):
		self.value=value
		self.next=None

class LinkedStack:
	#head指向栈顶
	def __init__(self):
		self.head=None
		self.size=0

	#节点进栈
	def pushNode(self,value):
		node=Node(value)
		#新节点指向栈顶
		node.next=self.head
		#栈顶指针head指向新节点
		self.head=node
		self.size+=1

	#弹出栈顶节点并返回值,空栈返回None
	def popNode(self):
		if self.isEmpty():
			return None
		#保存栈顶节点值
		value=self.head.value
		#栈顶指针指向下一个节点
		self.head=self.head.next
		self.size-=1
		return value

	#查看栈顶节点值,空栈返回None
	def peekNode(self):
		if self.isEmpty():
			return None
		return self.head.value

	#判断链栈是否为空
	def isEmpty(self):
		return self.head is None

	#获取链栈大小
	def getSize(self):
		return self.size

	#清空链栈
	def clear(self):
		self.head=None
		self.size=0

	#从栈顶到栈底输出链栈
	def show(self):
		values=[]
		current=self.head
		while current is not None:
			values.append(current.value)
			current=current.next
		print(f"Top [{','.join(map(str,values))}] Bottom")


