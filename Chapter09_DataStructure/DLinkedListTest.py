import random

import pytest

from Chapter09_DataStructure.DLinkedList import DLinkedList,Node


#检查双链表的正向、反向连接以及长度是否一致
def checkStructure(dLinkedList,expectedValues):
	assert dLinkedList.getLength()==len(expectedValues)
	assert dLinkedList.isEmpty()==(len(expectedValues)==0)
	assert dLinkedList.forwardToValue()==expectedValues
	assert dLinkedList.backwardToValue()==expectedValues[::-1]

	if len(expectedValues)==0:
		assert dLinkedList.head is None
		assert dLinkedList.tail is None
		return

	assert dLinkedList.head is not None
	assert dLinkedList.tail is not None
	assert dLinkedList.head.pre is None
	assert dLinkedList.tail.next is None
	assert dLinkedList.head.value==expectedValues[0]
	assert dLinkedList.tail.value==expectedValues[-1]

	current=dLinkedList.head
	previous=None
	index=0
	while current is not None:
		assert current.pre is previous
		assert current.value==expectedValues[index]
		previous=current
		current=current.next
		index+=1
	assert previous is dLinkedList.tail
	assert index==len(expectedValues)

	current=dLinkedList.tail
	nextNode=None
	index=len(expectedValues)-1
	while current is not None:
		assert current.next is nextNode
		assert current.value==expectedValues[index]
		nextNode=current
		current=current.pre
		index-=1
	assert nextNode is dLinkedList.head
	assert index==-1


#测试双链表节点的初始状态
def testNode():
	node=Node(10)
	assert node.value==10
	assert node.pre is None
	assert node.next is None


#测试空双链表的初始状态
def testEmptyDLinkedList():
	dLinkedList=DLinkedList()
	checkStructure(dLinkedList,[])
	assert dLinkedList.findNode(1) is None
	assert not dLinkedList.isContainsValue(1)
	assert dLinkedList.popHead() is None
	assert dLinkedList.popTail() is None
	assert not dLinkedList.removeNode(1)


#测试尾插一个节点
def testAppendSingleNode():
	dLinkedList=DLinkedList()
	dLinkedList.appendNode(10)
	checkStructure(dLinkedList,[10])
	assert dLinkedList.head is dLinkedList.tail


#测试连续尾插多个节点
def testAppendMultipleNodes():
	dLinkedList=DLinkedList()
	values=[1,2,3,4,5]
	for value in values:
		dLinkedList.appendNode(value)
	checkStructure(dLinkedList,values)


#测试头插一个节点
def testPrependSingleNode():
	dLinkedList=DLinkedList()
	dLinkedList.prependNode(10)
	checkStructure(dLinkedList,[10])
	assert dLinkedList.head is dLinkedList.tail


#测试连续头插多个节点
def testPrependMultipleNodes():
	dLinkedList=DLinkedList()
	for value in [1,2,3,4,5]:
		dLinkedList.prependNode(value)
	checkStructure(dLinkedList,[5,4,3,2,1])


#测试头插和尾插混合使用
def testAppendAndPrepend():
	dLinkedList=DLinkedList()
	dLinkedList.appendNode(2)
	dLinkedList.prependNode(1)
	dLinkedList.appendNode(3)
	dLinkedList.prependNode(0)
	checkStructure(dLinkedList,[0,1,2,3])


#测试按值查找节点以及包含关系
def testFindNodeAndContainsValue():
	dLinkedList=DLinkedList()
	for value in [10,20,30]:
		dLinkedList.appendNode(value)
	node=dLinkedList.findNode(20)
	assert isinstance(node,Node)
	assert node.value==20
	assert node.pre.value==10
	assert node.next.value==30
	assert dLinkedList.isContainsValue(30)
	assert not dLinkedList.isContainsValue(40)


#测试存在重复值时findNode返回第一个匹配节点
def testFindFirstDuplicateNode():
	dLinkedList=DLinkedList()
	for value in [1,2,2,3]:
		dLinkedList.appendNode(value)
	firstNode=dLinkedList.head.next
	secondNode=firstNode.next
	assert dLinkedList.findNode(2) is firstNode
	assert dLinkedList.findNode(2) is not secondNode


#测试根据索引获取节点和值
def testGetNodeAndValue():
	dLinkedList=DLinkedList()
	values=[10,20,30,40,50]
	for value in values:
		dLinkedList.appendNode(value)
	for index,value in enumerate(values):
		node=dLinkedList.getNode(index)
		assert isinstance(node,Node)
		assert node.value==value
		assert dLinkedList.getNodeValue(index)==value


#测试非法索引是否抛出异常
def testInvalidIndex():
	dLinkedList=DLinkedList()
	for value in [1,2,3]:
		dLinkedList.appendNode(value)
	for index in [-2,-1,3,4]:
		with pytest.raises(IndexError,match="Index out of range."):
			dLinkedList.getNode(index)
		with pytest.raises(IndexError,match="Index out of range."):
			dLinkedList.getNodeValue(index)
		with pytest.raises(IndexError,match="Index out of range."):
			dLinkedList.modifyNodeValue(index,100)


#测试修改指定索引节点的值
def testModifyNodeValue():
	dLinkedList=DLinkedList()
	for value in [1,2,3]:
		dLinkedList.appendNode(value)
	dLinkedList.modifyNodeValue(1,20)
	checkStructure(dLinkedList,[1,20,3])


#测试在中间节点和尾节点之后插入
def testInsertAfterNode():
	dLinkedList=DLinkedList()
	for value in [1,3,5]:
		dLinkedList.appendNode(value)
	assert dLinkedList.insertAfterNode(1,2)
	assert dLinkedList.insertAfterNode(3,4)
	assert dLinkedList.insertAfterNode(5,6)
	assert not dLinkedList.insertAfterNode(100,7)
	checkStructure(dLinkedList,[1,2,3,4,5,6])


#测试在中间节点和头节点之前插入
def testInsertBeforeNode():
	dLinkedList=DLinkedList()
	for value in [2,4,6]:
		dLinkedList.appendNode(value)
	assert dLinkedList.insertBeforeNode(2,1)
	assert dLinkedList.insertBeforeNode(4,3)
	assert dLinkedList.insertBeforeNode(6,5)
	assert not dLinkedList.insertBeforeNode(100,7)
	checkStructure(dLinkedList,[1,2,3,4,5,6])


#测试存在重复值时前插和后插作用于第一个匹配节点
def testInsertAroundFirstDuplicateNode():
	dLinkedList=DLinkedList()
	for value in [1,2,2,3]:
		dLinkedList.appendNode(value)
	assert dLinkedList.insertAfterNode(2,9)
	checkStructure(dLinkedList,[1,2,9,2,3])
	assert dLinkedList.insertBeforeNode(2,8)
	checkStructure(dLinkedList,[1,8,2,9,2,3])


#测试移除头节点
def testPopHead():
	dLinkedList=DLinkedList()
	for value in [1,2,3]:
		dLinkedList.appendNode(value)
	assert dLinkedList.popHead()==1
	checkStructure(dLinkedList,[2,3])
	assert dLinkedList.popHead()==2
	checkStructure(dLinkedList,[3])
	assert dLinkedList.popHead()==3
	checkStructure(dLinkedList,[])
	assert dLinkedList.popHead() is None


#测试移除尾节点
def testPopTail():
	dLinkedList=DLinkedList()
	for value in [1,2,3]:
		dLinkedList.appendNode(value)
	assert dLinkedList.popTail()==3
	checkStructure(dLinkedList,[1,2])
	assert dLinkedList.popTail()==2
	checkStructure(dLinkedList,[1])
	assert dLinkedList.popTail()==1
	checkStructure(dLinkedList,[])
	assert dLinkedList.popTail() is None


#测试根据值删除头节点、中间节点和尾节点
def testRemoveNode():
	dLinkedList=DLinkedList()
	for value in [1,2,3,4,5]:
		dLinkedList.appendNode(value)
	assert dLinkedList.removeNode(1)
	checkStructure(dLinkedList,[2,3,4,5])
	assert dLinkedList.removeNode(3)
	checkStructure(dLinkedList,[2,4,5])
	assert dLinkedList.removeNode(5)
	checkStructure(dLinkedList,[2,4])
	assert not dLinkedList.removeNode(100)
	checkStructure(dLinkedList,[2,4])


#测试存在重复值时删除第一个匹配节点
def testRemoveFirstDuplicateNode():
	dLinkedList=DLinkedList()
	for value in [1,2,2,3]:
		dLinkedList.appendNode(value)
	firstNode=dLinkedList.head.next
	secondNode=firstNode.next
	assert dLinkedList.removeNode(2)
	checkStructure(dLinkedList,[1,2,3])
	assert dLinkedList.head.next is secondNode


#测试正向和反向输出
def testPrintList(capsys):
	dLinkedList=DLinkedList()
	for value in [1,2,3]:
		dLinkedList.appendNode(value)
	dLinkedList.forwardPrintList()
	dLinkedList.backwardPrintList()
	output=capsys.readouterr().out
	assert output=="前向输出:[1, 2, 3]\n反向输出:[3, 2, 1]\n"


#测试清空双链表
def testClearList():
	dLinkedList=DLinkedList()
	for value in range(10):
		dLinkedList.appendNode(value)
	dLinkedList.clearList()
	checkStructure(dLinkedList,[])


#将双链表与Python列表执行一万次随机操作并比较结果
def testRandomOperationsAgainstList():
	randomGenerator=random.Random(2026)
	dLinkedList=DLinkedList()
	values=[]

	for _ in range(10000):
		operation=randomGenerator.randint(0,8)
		value=randomGenerator.randint(-50,50)

		if operation==0:
			dLinkedList.appendNode(value)
			values.append(value)

		elif operation==1:
			dLinkedList.prependNode(value)
			values.insert(0,value)

		elif operation==2:
			actualValue=dLinkedList.popHead()
			expectedValue=values.pop(0) if values else None
			assert actualValue==expectedValue

		elif operation==3:
			actualValue=dLinkedList.popTail()
			expectedValue=values.pop() if values else None
			assert actualValue==expectedValue

		elif operation==4:
			actualResult=dLinkedList.removeNode(value)
			if value in values:
				values.remove(value)
				expectedResult=True
			else:
				expectedResult=False
			assert actualResult==expectedResult

		elif operation==5:
			newValue=randomGenerator.randint(-100,100)
			actualResult=dLinkedList.insertAfterNode(value,newValue)
			if value in values:
				index=values.index(value)
				values.insert(index+1,newValue)
				expectedResult=True
			else:
				expectedResult=False
			assert actualResult==expectedResult

		elif operation==6:
			newValue=randomGenerator.randint(-100,100)
			actualResult=dLinkedList.insertBeforeNode(value,newValue)
			if value in values:
				index=values.index(value)
				values.insert(index,newValue)
				expectedResult=True
			else:
				expectedResult=False
			assert actualResult==expectedResult

		elif operation==7:
			assert dLinkedList.isContainsValue(value)==(value in values)
			node=dLinkedList.findNode(value)
			if value in values:
				assert node is not None
				assert node.value==value
			else:
				assert node is None

		else:
			if values:
				index=randomGenerator.randrange(len(values))
				newValue=randomGenerator.randint(-100,100)
				dLinkedList.modifyNodeValue(index,newValue)
				values[index]=newValue
			elif randomGenerator.random()<0.05:
				dLinkedList.clearList()
				values.clear()

		checkStructure(dLinkedList,values)

		if values:
			index=randomGenerator.randrange(len(values))
			assert dLinkedList.getNodeValue(index)==values[index]
