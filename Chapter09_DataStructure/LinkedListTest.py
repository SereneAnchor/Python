import random

from Chapter09_DataStructure.LinkedList import LinkedList,Node


#将链表中的所有节点值转换成Python列表,同时检查链表中是否存在环
def getValues(linkedList):
	values=[]
	visited=set()
	current=linkedList.head
	while current is not None:
		currentId=id(current)
		assert currentId not in visited,"链表中存在环"
		visited.add(currentId)
		values.append(current.value)
		current=current.next
	return values


#获取链表中指定索引处的节点
def getNodeAt(linkedList,index):
	current=linkedList.head
	for _ in range(index):
		current=current.next
	return current


#测试新建节点的数据域和指针域是否正确
def testNodeCreation():
	node=Node(100)
	assert node.value==100
	assert node.next is None


#测试新建链表的初始状态是否正确
def testEmptyLinkedList():
	linkedList=LinkedList()
	assert linkedList.head is None
	assert linkedList.isEmpty()
	assert getValues(linkedList)==[]


#测试在链表尾部连续插入节点后顺序是否正确
def testAppendNode():
	linkedList=LinkedList()
	values=[1,2,3,4]
	for value in values:
		linkedList.appendNode(value)
	assert getValues(linkedList)==values
	assert linkedList.head.value==1
	assert not linkedList.isEmpty()


#测试在链表头部连续插入节点后顺序是否正确
def testPrependNode():
	linkedList=LinkedList()
	values=[1,2,3,4]
	for value in values:
		linkedList.prependNode(value)
	assert getValues(linkedList)==values[::-1]
	assert linkedList.head.value==4


#测试头插和尾插交替执行时链表顺序是否正确
def testAppendAndPrepend():
	linkedList=LinkedList()
	linkedList.appendNode(20)
	linkedList.prependNode(10)
	linkedList.appendNode(30)
	linkedList.prependNode(0)
	assert getValues(linkedList)==[0,10,20,30]


#测试查找头节点、中间节点、尾节点和不存在的节点
def testFindNode():
	linkedList=LinkedList()
	values=[10,20,30]
	for value in values:
		linkedList.appendNode(value)
	assert linkedList.findNode(10) is linkedList.head
	assert linkedList.findNode(20) is linkedList.head.next
	assert linkedList.findNode(30) is linkedList.head.next.next
	assert linkedList.findNode(100) is None


#测试存在重复值时findNode是否返回第一个匹配节点
def testFindDuplicateNode():
	linkedList=LinkedList()
	values=[1,2,1,3]
	for value in values:
		linkedList.appendNode(value)
	result=linkedList.findNode(1)
	assert result is linkedList.head
	assert result.value==1


#测试空链表删除节点时返回False且链表状态保持不变
def testRemoveNodeFromEmptyList():
	linkedList=LinkedList()
	assert linkedList.removeNode(10) is False
	assert linkedList.isEmpty()
	assert getValues(linkedList)==[]


#测试删除头节点后head是否正确指向下一个节点
def testRemoveHeadNode():
	linkedList=LinkedList()
	for value in [1,2,3]:
		linkedList.appendNode(value)
	assert linkedList.removeNode(1) is True
	assert getValues(linkedList)==[2,3]
	assert linkedList.head.value==2


#测试删除中间节点后前后节点是否正确连接
def testRemoveMiddleNode():
	linkedList=LinkedList()
	for value in [1,2,3,4]:
		linkedList.appendNode(value)
	assert linkedList.removeNode(3) is True
	assert getValues(linkedList)==[1,2,4]
	assert linkedList.head.next.next.value==4


#测试删除尾节点后新的尾节点是否指向None
def testRemoveTailNode():
	linkedList=LinkedList()
	for value in [1,2,3]:
		linkedList.appendNode(value)
	assert linkedList.removeNode(3) is True
	assert getValues(linkedList)==[1,2]
	assert linkedList.head.next.next is None


#测试删除不存在的节点时返回False且链表内容保持不变
def testRemoveMissingNode():
	linkedList=LinkedList()
	for value in [1,2,3]:
		linkedList.appendNode(value)
	assert linkedList.removeNode(100) is False
	assert getValues(linkedList)==[1,2,3]


#测试存在重复值时removeNode是否只删除第一个匹配节点
def testRemoveDuplicateNode():
	linkedList=LinkedList()
	for value in [1,2,1,3]:
		linkedList.appendNode(value)
	assert linkedList.removeNode(1) is True
	assert getValues(linkedList)==[2,1,3]


#测试删除链表中唯一节点后链表是否变为空
def testRemoveOnlyNode():
	linkedList=LinkedList()
	linkedList.appendNode(10)
	assert linkedList.removeNode(10) is True
	assert linkedList.head is None
	assert linkedList.isEmpty()


#测试输出空链表和非空链表时显示的内容是否正确
def testPrintLinkedList(capsys):
	linkedList=LinkedList()
	linkedList.show()
	for value in [1,2,3]:
		linkedList.appendNode(value)
	linkedList.show()
	output=capsys.readouterr().out
	assert output=="输出链表:[]\n输出链表:[1, 2, 3]\n"


#将自定义链表与Python列表执行一万次随机操作并比较结果
def testRandomOperationsAgainstList():
	randomGenerator=random.Random(2026)
	linkedList=LinkedList()
	standardList=[]
	for _ in range(10000):
		operation=randomGenerator.randint(0,3)
		if operation==0:
			value=randomGenerator.randint(-1000,1000)
			linkedList.appendNode(value)
			standardList.append(value)
		elif operation==1:
			value=randomGenerator.randint(-1000,1000)
			linkedList.prependNode(value)
			standardList.insert(0,value)
		elif operation==2:
			if standardList and randomGenerator.random()<0.7:
				value=randomGenerator.choice(standardList)
			else:
				value=randomGenerator.randint(-1000,1000)
			expectedResult=value in standardList
			actualResult=linkedList.removeNode(value)
			assert actualResult==expectedResult
			if expectedResult:
				standardList.remove(value)
		else:
			if standardList and randomGenerator.random()<0.7:
				value=randomGenerator.choice(standardList)
			else:
				value=randomGenerator.randint(-1000,1000)
			result=linkedList.findNode(value)
			if value in standardList:
				expectedIndex=standardList.index(value)
				assert result is getNodeAt(linkedList,expectedIndex)
			else:
				assert result is None
		assert getValues(linkedList)==standardList
		assert linkedList.isEmpty()==(len(standardList)==0)
