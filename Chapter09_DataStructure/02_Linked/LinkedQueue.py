#链式队列

class Node:
	def __init__(self,value):
		self.value=value
		self.next=None

class LinkedQueue:
	def __init__(self):
		self.head=None
		self.tail=None
		self.size=0

	#节点进队
	def enqueueNode(self,value):
		node=Node(value)
		#队尾为空说明是空队
		if self.tail is None:
			self.head=node
			self.tail=node
		#把新节点添加到队尾,让原队尾指向新节点
		else:
			self.tail.next=node
			self.tail=node
		self.size+=1

	#弹出队头节点并返回值,空队返回None
	def dequeueNode(self):
		if self.isEmpty():
			return None
		#保存队头节点值
		value=self.head.value
		#队头指针指向下一个节点
		self.head=self.head.next
		#如果下一个节点为空,说明队中只有一个节点
		if self.head is None:
			self.tail=None
		self.size-=1
		return value

	#查看队头节点值,空队返回None
	def peekNode(self):
		if self.isEmpty():
			return None
		return self.head.value

	#判断链队是否为空
	def isEmpty(self):
		return self.head is None

	#获取链队大小
	def getSize(self):
		return self.size

	#清空链队
	def clear(self):
		self.head=None
		self.tail=None
		self.size=0

	#输出链式队列
	def show(self):
		values=[]
		current=self.head
		while current is not None:
			values.append(current.value)
			current=current.next
		print(f"Front [{','.join(map(str,values))}] Rear")
