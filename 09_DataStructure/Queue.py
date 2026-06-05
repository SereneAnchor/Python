#队列

class Queue:
	#使用列表来存储队列元素
	def __init__(self):
		self.items=[]

	#元素进队
	def enqueueItem(self,value):
		self.items.append(value)

	#元素出队(不返回队首元素)
	def dequeueItem(self):
		if self.isEmpty():
			return None
		return self.items.pop(0)

	#获取队头元素
	def peekItem(self):
		if self.isEmpty():
			return None
		return self.items[0]

	#获取队列长度
	def getLength(self):
		return len(self.items)

	#判断队列是否为空
	def isEmpty(self):
		return len(self.items)==0

	#输出队列
	def printQueue(self):
		print(f"输出队列:{self.items}")


if __name__=="__main__":
	#创建队列,队列中无任何元素
	queue=Queue()
	print(f"队列为空:{queue.isEmpty()}")

	#元素进队
	queue.enqueueItem('A')
	queue.enqueueItem('B')
	queue.enqueueItem('C')
	queue.printQueue()

	print(f"获取队头:{queue.peekItem()}")
	print(f"移除队头:{queue.dequeueItem()}")
	queue.printQueue()

	#获取队长
	print(f"队列长度:{queue.getLength()}")


