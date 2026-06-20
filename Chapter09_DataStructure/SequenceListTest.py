import random

import pytest

from Chapter09_DataStructure.SequenceList import SequenceList


#测试新建顺序表的初始状态是否正确
def testEmptyList():
	sequenceList=SequenceList()
	assert sequenceList.isEmpty()
	assert sequenceList.getLength()==0
	assert sequenceList.items==[]


#测试在顺序表末尾添加元素后,长度、内容和判空结果是否正确
def testAppendItem():
	sequenceList=SequenceList()
	values=[5,3,8,1,-2]
	for value in values:
		sequenceList.appendItem(value)
	assert sequenceList.getLength()==len(values)
	assert sequenceList.items==values
	assert not sequenceList.isEmpty()


#测试在顺序表开头、中间和末尾插入元素
def testInsertItem():
	sequenceList=SequenceList()
	sequenceList.insertItem(0,20)
	sequenceList.insertItem(0,10)
	sequenceList.insertItem(2,40)
	sequenceList.insertItem(2,30)
	assert sequenceList.items==[10,20,30,40]
	assert sequenceList.getLength()==4


#测试插入时使用负数或超过顺序表长度的索引会抛出异常
def testInsertItemWithInvalidIndex():
	sequenceList=SequenceList()
	sequenceList.appendItem(10)
	with pytest.raises(IndexError,match="索引-1越界,无法插入!"):
		sequenceList.insertItem(-1,20)
	with pytest.raises(IndexError,match="索引2越界,无法插入!"):
		sequenceList.insertItem(2,20)
	assert sequenceList.items==[10]


#测试删除存在的元素后,顺序表内容和长度是否正确
def testRemoveItem():
	sequenceList=SequenceList()
	values=[1,2,3,4]
	for value in values:
		sequenceList.appendItem(value)
	sequenceList.removeItem(3)
	assert sequenceList.items==[1,2,4]
	assert sequenceList.getLength()==3


#测试存在重复元素时只删除第一个出现的元素
def testRemoveDuplicateValue():
	sequenceList=SequenceList()
	values=[1,2,1,3]
	for value in values:
		sequenceList.appendItem(value)
	sequenceList.removeItem(1)
	assert sequenceList.items==[2,1,3]


#测试删除不存在的元素时会抛出自定义异常
def testRemoveMissingValue():
	sequenceList=SequenceList()
	sequenceList.appendItem(10)
	with pytest.raises(ValueError,match="20不存在,无法删除!"):
		sequenceList.removeItem(20)
	assert sequenceList.items==[10]


#测试修改指定索引处的元素后,内容和长度是否正确
def testModifyItem():
	sequenceList=SequenceList()
	values=[10,20,30]
	for value in values:
		sequenceList.appendItem(value)
	sequenceList.modifyItem(1,200)
	assert sequenceList.items==[10,200,30]
	assert sequenceList.getLength()==3


#测试修改时使用负数或不存在的索引会抛出异常
def testModifyItemWithInvalidIndex():
	sequenceList=SequenceList()
	sequenceList.appendItem(10)
	with pytest.raises(IndexError,match="索引-1越界,无法修改!"):
		sequenceList.modifyItem(-1,20)
	with pytest.raises(IndexError,match="索引1越界,无法修改!"):
		sequenceList.modifyItem(1,20)
	assert sequenceList.items==[10]


#测试获取指定索引处的元素时不会修改顺序表
def testGetItem():
	sequenceList=SequenceList()
	values=[10,20,30]
	for value in values:
		sequenceList.appendItem(value)
	assert sequenceList.getItem(0)==10
	assert sequenceList.getItem(2)==30
	assert sequenceList.items==values
	assert sequenceList.getLength()==3


#测试获取时使用负数或不存在的索引会抛出异常
def testGetItemWithInvalidIndex():
	sequenceList=SequenceList()
	sequenceList.appendItem(10)
	with pytest.raises(IndexError,match="索引-1越界,无法获取!"):
		sequenceList.getItem(-1)
	with pytest.raises(IndexError,match="索引1越界,无法获取!"):
		sequenceList.getItem(1)


#测试查找存在、重复和不存在的元素时返回结果是否正确
def testFindItem():
	sequenceList=SequenceList()
	values=[5,3,8,3]
	for value in values:
		sequenceList.appendItem(value)
	assert sequenceList.findItem(5)==0
	assert sequenceList.findItem(3)==1
	assert sequenceList.findItem(8)==2
	assert sequenceList.findItem(100)==-1


#测试输出顺序表时显示的内容是否正确
def testPrintList(capsys):
	sequenceList=SequenceList()
	values=[1,2,3]
	for value in values:
		sequenceList.appendItem(value)
	sequenceList.show()
	output=capsys.readouterr().out
	assert output=="输出顺序表:[1, 2, 3]\n"


#将自定义顺序表与Python列表执行一万次随机操作并比较结果
def testRandomOperationsAgainstList():
	randomGenerator=random.Random(2026)
	myList=SequenceList()
	standardList=[]
	for _ in range(10000):
		operation=randomGenerator.randint(0,5)
		if operation==0:
			value=randomGenerator.randint(-10000,10000)
			myList.appendItem(value)
			standardList.append(value)
		elif operation==1:
			value=randomGenerator.randint(-10000,10000)
			index=randomGenerator.randint(0,len(standardList))
			myList.insertItem(index,value)
			standardList.insert(index,value)
		elif operation==2 and standardList:
			value=randomGenerator.choice(standardList)
			myList.removeItem(value)
			standardList.remove(value)
		elif operation==3 and standardList:
			index=randomGenerator.randrange(len(standardList))
			value=randomGenerator.randint(-10000,10000)
			myList.modifyItem(index,value)
			standardList[index]=value
		elif operation==4 and standardList:
			index=randomGenerator.randrange(len(standardList))
			assert myList.getItem(index)==standardList[index]
		elif operation==5:
			value=randomGenerator.randint(-10000,10000)
			try:
				expectedIndex=standardList.index(value)
			except ValueError:
				expectedIndex=-1
			assert myList.findItem(value)==expectedIndex
		assert myList.items==standardList
		assert myList.getLength()==len(standardList)
		assert myList.isEmpty()==(len(standardList)==0)
