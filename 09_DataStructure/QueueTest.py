from Queue import Queue

def runTest():
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

if __name__=="__main__":
	runTest()