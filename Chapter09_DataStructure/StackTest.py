import random

from Chapter09_DataStructure.Stack import Stack


#测试新建栈的初始状态是否正确
def testEmptyStack():
	stack=Stack()
	assert stack.isEmpty()
	assert stack.getLength()==0


#测试元素进栈后栈顶、栈长度和元素完整性是否正确
def testPushItem():
	stack=Stack()
	values=[5,3,8,1,-2]
	for value in values:
		stack.pushItem(value)
	assert stack.getLength()==len(values)
	assert stack.peekItem()==values[-1]
	assert stack.items==values
	assert not stack.isEmpty()


#测试连续出栈是否遵循后进先出的顺序
def testPopItem():
	stack=Stack()
	values=[5,3,8,1,-2]
	for value in values:
		stack.pushItem(value)
	result=[]
	while not stack.isEmpty():
		result.append(stack.popItem())
	assert result==values[::-1]
	assert stack.getLength()==0
	assert stack.isEmpty()


#测试获取栈顶元素时是否不会删除栈顶元素
def testPeekItemDoesNotRemove():
	stack=Stack()
	stack.pushItem(10)
	stack.pushItem(20)
	value=stack.peekItem()
	assert value==20
	assert stack.getLength()==2
	assert stack.items==[10,20]


#测试只有一个元素时的进栈、查看和出栈操作
def testSingleItem():
	stack=Stack()
	stack.pushItem(100)
	assert stack.getLength()==1
	assert stack.peekItem()==100
	assert stack.popItem()==100
	assert stack.getLength()==0
	assert stack.isEmpty()


#测试空栈调用popItem时返回None并输出提示
def testPopItemOnEmptyStack(capsys):
	stack=Stack()
	result=stack.popItem()
	output=capsys.readouterr().out
	assert result is None
	assert output=="栈空.\n"
	assert stack.isEmpty()


#测试空栈调用peekItem时返回None并输出提示
def testPeekItemOnEmptyStack(capsys):
	stack=Stack()
	result=stack.peekItem()
	output=capsys.readouterr().out
	assert result is None
	assert output=="栈空.\n"
	assert stack.isEmpty()


#测试输出栈时显示的内容是否正确
def testPrintStack(capsys):
	stack=Stack()
	values=[1,2,3]
	for value in values:
		stack.pushItem(value)
	stack.printStack()
	output=capsys.readouterr().out
	assert output=="输出栈:[1, 2, 3]\n"


#将自定义栈与Python列表执行一万次随机操作并比较结果
def testRandomOperationsAgainstList():
	randomGenerator=random.Random(2026)
	myStack=Stack()
	standardStack=[]
	for _ in range(10000):
		shouldPush=(len(standardStack)==0 or randomGenerator.random()<0.6)
		if shouldPush:
			value=randomGenerator.randint(-10000,10000)
			myStack.pushItem(value)
			standardStack.append(value)
		else:
			myResult=myStack.popItem()
			standardResult=standardStack.pop()
			assert myResult==standardResult
		assert myStack.getLength()==len(standardStack)
		assert myStack.isEmpty()==(len(standardStack)==0)
		if standardStack:
			assert myStack.peekItem()==standardStack[-1]
	while standardStack:
		assert myStack.popItem()==standardStack.pop()
	assert myStack.isEmpty()
	assert myStack.getLength()==0
