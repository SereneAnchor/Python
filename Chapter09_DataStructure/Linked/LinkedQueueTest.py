import random

from Chapter09_DataStructure.Linked.LinkedQueue import LinkedQueue,Node


#检查链队的节点顺序、头尾指针、长度以及是否存在循环
def checkStructure(linkedQueue,expectedValues):
	assert linkedQueue.getSize()==len(expectedValues)
	assert linkedQueue.isEmpty()==(len(expectedValues)==0)

	if len(expectedValues)==0:
		assert linkedQueue.head is None
		assert linkedQueue.tail is None
		return

	assert linkedQueue.head is not None
	assert linkedQueue.tail is not None
	assert linkedQueue.head.value==expectedValues[0]
	assert linkedQueue.tail.value==expectedValues[-1]
	assert linkedQueue.tail.next is None

	actualValues=[]
	visitedNodes=set()
	current=linkedQueue.head
	lastNode=None

	while current is not None:
		nodeId=id(current)
		assert nodeId not in visitedNodes
		visitedNodes.add(nodeId)
		actualValues.append(current.value)
		lastNode=current
		current=current.next

	assert actualValues==expectedValues
	assert lastNode is linkedQueue.tail
	assert len(actualValues)==linkedQueue.getSize()


#测试节点的初始状态
def testNode():
	node=Node(10)
	assert node.value==10
	assert node.next is None


#测试空链队的初始状态
def testEmptyLinkedQueue():
	linkedQueue=LinkedQueue()
	assert linkedQueue.head is None
	assert linkedQueue.tail is None
	assert linkedQueue.isEmpty()
	assert linkedQueue.getSize()==0
	assert linkedQueue.peekNode() is None
	assert linkedQueue.dequeueNode() is None
	checkStructure(linkedQueue,[])


#测试一个节点进队
def testEnqueueSingleNode():
	linkedQueue=LinkedQueue()
	linkedQueue.enqueueNode(10)
	assert linkedQueue.head is linkedQueue.tail
	assert linkedQueue.peekNode()==10
	checkStructure(linkedQueue,[10])


#测试多个节点连续进队
def testEnqueueMultipleNodes():
	linkedQueue=LinkedQueue()
	values=[1,2,3,4,5]

	for value in values:
		linkedQueue.enqueueNode(value)

	assert linkedQueue.peekNode()==1
	checkStructure(linkedQueue,values)


#测试先进先出的出队顺序
def testDequeueNodeFifo():
	linkedQueue=LinkedQueue()

	for value in [1,2,3,4,5]:
		linkedQueue.enqueueNode(value)

	assert linkedQueue.dequeueNode()==1
	assert linkedQueue.dequeueNode()==2
	assert linkedQueue.dequeueNode()==3
	assert linkedQueue.dequeueNode()==4
	assert linkedQueue.dequeueNode()==5
	assert linkedQueue.dequeueNode() is None
	checkStructure(linkedQueue,[])


#测试查看队头值不会修改链队
def testPeekNodeWithoutRemoving():
	linkedQueue=LinkedQueue()

	for value in [10,20,30]:
		linkedQueue.enqueueNode(value)

	oldHead=linkedQueue.head
	oldTail=linkedQueue.tail
	oldSize=linkedQueue.getSize()

	assert linkedQueue.peekNode()==10
	assert linkedQueue.peekNode()==10
	assert linkedQueue.head is oldHead
	assert linkedQueue.tail is oldTail
	assert linkedQueue.getSize()==oldSize
	checkStructure(linkedQueue,[10,20,30])


#测试进队和出队混合操作
def testEnqueueAndDequeueMixed():
	linkedQueue=LinkedQueue()
	values=[]

	linkedQueue.enqueueNode(1)
	values.append(1)

	linkedQueue.enqueueNode(2)
	values.append(2)

	assert linkedQueue.dequeueNode()==values.pop(0)

	linkedQueue.enqueueNode(3)
	values.append(3)

	linkedQueue.enqueueNode(4)
	values.append(4)

	assert linkedQueue.dequeueNode()==values.pop(0)
	assert linkedQueue.peekNode()==values[0]

	checkStructure(linkedQueue,values)


#测试最后一个节点出队后头尾指针是否同时清空
def testDequeueLastNode():
	linkedQueue=LinkedQueue()
	linkedQueue.enqueueNode(10)

	assert linkedQueue.dequeueNode()==10
	assert linkedQueue.head is None
	assert linkedQueue.tail is None
	assert linkedQueue.getSize()==0
	assert linkedQueue.isEmpty()


#测试保存None值时链队状态是否正确
def testStoreNoneValue():
	linkedQueue=LinkedQueue()
	linkedQueue.enqueueNode(None)

	assert not linkedQueue.isEmpty()
	assert linkedQueue.getSize()==1
	assert linkedQueue.peekNode() is None
	assert linkedQueue.dequeueNode() is None
	assert linkedQueue.isEmpty()
	assert linkedQueue.getSize()==0


#测试清空链队
def testClear():
	linkedQueue=LinkedQueue()

	for value in range(100):
		linkedQueue.enqueueNode(value)

	linkedQueue.clear()

	assert linkedQueue.head is None
	assert linkedQueue.tail is None
	assert linkedQueue.isEmpty()
	assert linkedQueue.getSize()==0
	assert linkedQueue.peekNode() is None
	assert linkedQueue.dequeueNode() is None
	checkStructure(linkedQueue,[])


#测试空链队和非空链队的输出格式
def testShow(capsys):
	linkedQueue=LinkedQueue()

	linkedQueue.show()
	emptyOutput=capsys.readouterr().out
	assert emptyOutput=="Front [] Rear\n"

	for value in [1,2,3]:
		linkedQueue.enqueueNode(value)

	linkedQueue.show()
	output=capsys.readouterr().out
	assert output=="Front [1,2,3] Rear\n"


#测试不同类型的值是否能够正常输出
def testShowDifferentValueTypes(capsys):
	linkedQueue=LinkedQueue()

	for value in [1,"Python",True,None]:
		linkedQueue.enqueueNode(value)

	linkedQueue.show()
	output=capsys.readouterr().out
	assert output=="Front [1,Python,True,None] Rear\n"


#测试大量节点连续进队和出队
def testLargeQueue():
	linkedQueue=LinkedQueue()
	values=list(range(5000))

	for value in values:
		linkedQueue.enqueueNode(value)

	checkStructure(linkedQueue,values)

	for expectedValue in values:
		assert linkedQueue.dequeueNode()==expectedValue

	checkStructure(linkedQueue,[])


#将链队与Python列表执行一万次随机操作并比较结果
def testRandomOperationsAgainstList():
	randomGenerator=random.Random(2026)
	linkedQueue=LinkedQueue()
	values=[]

	for i in range(10000):
		operation=randomGenerator.randint(0,4)

		if operation<=1:
			value=randomGenerator.randint(-1000,1000)
			linkedQueue.enqueueNode(value)
			values.append(value)

		elif operation==2:
			actualValue=linkedQueue.dequeueNode()
			expectedValue=values.pop(0) if values else None
			assert actualValue==expectedValue

		elif operation==3:
			actualValue=linkedQueue.peekNode()
			expectedValue=values[0] if values else None
			assert actualValue==expectedValue

		else:
			if randomGenerator.random()<0.05:
				linkedQueue.clear()
				values.clear()

		checkStructure(linkedQueue,values)
