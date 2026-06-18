import random
from collections import deque

from Chapter09_DataStructure.Queue import Queue


#测试新建队列的初始状态是否正确
def testEmptyQueue():
	queue=Queue()
	assert queue.isEmpty()
	assert queue.getLength()==0
	assert queue.peekItem() is None
	assert queue.dequeueItem() is None


#测试元素进队后队头、队列长度、元素完整性和判空结果是否正确
def testEnqueueItem():
	queue=Queue()
	values=[5,3,8,1,-2]
	for value in values:
		queue.enqueueItem(value)
	assert queue.getLength()==len(values)
	assert queue.peekItem()==values[0]
	assert queue.items==values
	assert not queue.isEmpty()


#测试连续出队是否遵循先进先出的顺序
def testDequeueItem():
	queue=Queue()
	values=[5,3,8,1,-2]
	for value in values:
		queue.enqueueItem(value)
	result=[]
	while not queue.isEmpty():
		result.append(queue.dequeueItem())
	assert result==values
	assert queue.getLength()==0
	assert queue.isEmpty()


#测试获取队头元素时是否不会删除队头元素
def testPeekItemDoesNotRemove():
	queue=Queue()
	queue.enqueueItem(10)
	queue.enqueueItem(20)
	value=queue.peekItem()
	assert value==10
	assert queue.getLength()==2
	assert queue.items==[10,20]


#测试只有一个元素时的进队、查看和出队操作
def testSingleItem():
	queue=Queue()
	queue.enqueueItem(100)
	assert queue.getLength()==1
	assert queue.peekItem()==100
	assert queue.dequeueItem()==100
	assert queue.getLength()==0
	assert queue.isEmpty()
	assert queue.peekItem() is None
	assert queue.dequeueItem() is None


#测试空队列调用dequeueItem时返回None且队列状态保持不变
def testDequeueItemOnEmptyQueue():
	queue=Queue()
	result=queue.dequeueItem()
	assert result is None
	assert queue.getLength()==0
	assert queue.isEmpty()


#测试空队列调用peekItem时返回None且队列状态保持不变
def testPeekItemOnEmptyQueue():
	queue=Queue()
	result=queue.peekItem()
	assert result is None
	assert queue.getLength()==0
	assert queue.isEmpty()


#测试多次进队和出队交替执行时顺序是否正确
def testMixedOperations():
	queue=Queue()
	queue.enqueueItem(10)
	queue.enqueueItem(20)
	assert queue.dequeueItem()==10
	queue.enqueueItem(30)
	queue.enqueueItem(40)
	assert queue.peekItem()==20
	assert queue.dequeueItem()==20
	assert queue.dequeueItem()==30
	assert queue.dequeueItem()==40
	assert queue.isEmpty()


#测试输出队列时显示的内容是否正确
def testPrintQueue(capsys):
	queue=Queue()
	values=[1,2,3]
	for value in values:
		queue.enqueueItem(value)
	queue.printQueue()
	output=capsys.readouterr().out
	assert output=="输出队列:[1, 2, 3]\n"


#将自定义队列与Python的deque执行一万次随机操作并比较结果
def testRandomOperationsAgainstDeque():
	randomGenerator=random.Random(2026)
	myQueue=Queue()
	standardQueue=deque()
	for _ in range(10000):
		shouldEnqueue=(len(standardQueue)==0 or randomGenerator.random()<0.6)
		if shouldEnqueue:
			value=randomGenerator.randint(-10000,10000)
			myQueue.enqueueItem(value)
			standardQueue.append(value)
		else:
			myResult=myQueue.dequeueItem()
			standardResult=standardQueue.popleft()
			assert myResult==standardResult
		assert myQueue.getLength()==len(standardQueue)
		assert myQueue.isEmpty()==(len(standardQueue)==0)
		if standardQueue:
			assert myQueue.peekItem()==standardQueue[0]
		else:
			assert myQueue.peekItem() is None
	while standardQueue:
		assert myQueue.dequeueItem()==standardQueue.popleft()
	assert myQueue.isEmpty()
	assert myQueue.getLength()==0
