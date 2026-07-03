import random
from importlib import import_module
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[2]))

module=import_module("Chapter09_DataStructure.02_Linked.03_LinkedStack")
LinkedStack=module.LinkedStack
Node=module.Node


#检查链栈的节点顺序、长度以及是否存在循环
def checkStructure(linkedStack,expectedValues):
	assert linkedStack.getSize()==len(expectedValues)
	assert linkedStack.isEmpty()==(len(expectedValues)==0)

	if len(expectedValues)==0:
		assert linkedStack.head is None
		return

	assert linkedStack.head is not None
	assert linkedStack.head.value==expectedValues[-1]

	actualValues=[]
	visitedNodes=set()
	current=linkedStack.head

	while current is not None:
		nodeId=id(current)
		assert nodeId not in visitedNodes
		visitedNodes.add(nodeId)
		actualValues.append(current.value)
		current=current.next

	assert actualValues==expectedValues[::-1]
	assert len(actualValues)==linkedStack.getSize()


#测试节点的初始状态
def testNode():
	node=Node(10)
	assert node.value==10
	assert node.next is None


#测试空链栈的初始状态
def testEmptyLinkedStack():
	linkedStack=LinkedStack()
	assert linkedStack.head is None
	assert linkedStack.isEmpty()
	assert linkedStack.getSize()==0
	assert linkedStack.peekNode() is None
	assert linkedStack.popNode() is None
	checkStructure(linkedStack,[])


#测试压入一个节点
def testPushSingleNode():
	linkedStack=LinkedStack()
	linkedStack.pushNode(10)
	assert linkedStack.head.value==10
	assert linkedStack.head.next is None
	assert linkedStack.peekNode()==10
	checkStructure(linkedStack,[10])


#测试连续压入多个节点
def testPushMultipleNodes():
	linkedStack=LinkedStack()
	values=[1,2,3,4,5]

	for value in values:
		linkedStack.pushNode(value)

	assert linkedStack.peekNode()==5
	checkStructure(linkedStack,values)


#测试后进先出的出栈顺序
def testPopNodeLifo():
	linkedStack=LinkedStack()

	for value in [1,2,3,4,5]:
		linkedStack.pushNode(value)

	assert linkedStack.popNode()==5
	assert linkedStack.popNode()==4
	assert linkedStack.popNode()==3
	assert linkedStack.popNode()==2
	assert linkedStack.popNode()==1
	assert linkedStack.popNode() is None
	checkStructure(linkedStack,[])


#测试查看栈顶值不会修改链栈
def testPeekNodeWithoutRemoving():
	linkedStack=LinkedStack()

	for value in [10,20,30]:
		linkedStack.pushNode(value)

	oldHead=linkedStack.head
	oldSize=linkedStack.getSize()

	assert linkedStack.peekNode()==30
	assert linkedStack.peekNode()==30
	assert linkedStack.head is oldHead
	assert linkedStack.getSize()==oldSize
	checkStructure(linkedStack,[10,20,30])


#测试入栈和出栈混合操作
def testPushAndPopMixed():
	linkedStack=LinkedStack()
	values=[]

	linkedStack.pushNode(1)
	values.append(1)

	linkedStack.pushNode(2)
	values.append(2)

	assert linkedStack.popNode()==values.pop()

	linkedStack.pushNode(3)
	values.append(3)

	linkedStack.pushNode(4)
	values.append(4)

	assert linkedStack.popNode()==values.pop()
	assert linkedStack.peekNode()==values[-1]

	checkStructure(linkedStack,values)


#测试保存None值时链栈状态是否正确
def testStoreNoneValue():
	linkedStack=LinkedStack()
	linkedStack.pushNode(None)

	assert not linkedStack.isEmpty()
	assert linkedStack.getSize()==1
	assert linkedStack.peekNode() is None
	assert linkedStack.popNode() is None
	assert linkedStack.isEmpty()
	assert linkedStack.getSize()==0


#测试清空链栈
def testClear():
	linkedStack=LinkedStack()

	for value in range(100):
		linkedStack.pushNode(value)

	linkedStack.clear()

	assert linkedStack.head is None
	assert linkedStack.isEmpty()
	assert linkedStack.getSize()==0
	assert linkedStack.peekNode() is None
	assert linkedStack.popNode() is None
	checkStructure(linkedStack,[])


#测试空链栈和非空链栈的输出格式
def testShow(capsys):
	linkedStack=LinkedStack()

	linkedStack.show()
	emptyOutput=capsys.readouterr().out
	assert emptyOutput=="Top [] Bottom\n"

	for value in [1,2,3]:
		linkedStack.pushNode(value)

	linkedStack.show()
	output=capsys.readouterr().out
	assert output=="Top [3,2,1] Bottom\n"


#测试不同类型的值是否能够正常输出
def testShowDifferentValueTypes(capsys):
	linkedStack=LinkedStack()

	for value in [1,"Python",True,None]:
		linkedStack.pushNode(value)

	linkedStack.show()
	output=capsys.readouterr().out
	assert output=="Top [None,True,Python,1] Bottom\n"


#测试大量节点连续入栈和出栈
def testLargeStack():
	linkedStack=LinkedStack()
	values=list(range(5000))

	for value in values:
		linkedStack.pushNode(value)

	checkStructure(linkedStack,values)

	for expectedValue in reversed(values):
		assert linkedStack.popNode()==expectedValue

	checkStructure(linkedStack,[])


#将链栈与Python列表执行一万次随机操作并比较结果
def testRandomOperationsAgainstList():
	randomGenerator=random.Random(2026)
	linkedStack=LinkedStack()
	values=[]

	for _ in range(10000):
		operation=randomGenerator.randint(0,4)

		if operation<=1:
			value=randomGenerator.randint(-1000,1000)
			linkedStack.pushNode(value)
			values.append(value)

		elif operation==2:
			actualValue=linkedStack.popNode()
			expectedValue=values.pop() if values else None
			assert actualValue==expectedValue

		elif operation==3:
			actualValue=linkedStack.peekNode()
			expectedValue=values[-1] if values else None
			assert actualValue==expectedValue

		else:
			if randomGenerator.random()<0.05:
				linkedStack.clear()
				values.clear()

		checkStructure(linkedStack,values)
