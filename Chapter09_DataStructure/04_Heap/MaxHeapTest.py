import heapq
import random

from Chapter09_DataStructure.Heap.MaxHeap import MaxHeap


#检查当前堆是否满足最大堆性质,即每个父节点都大于或等于它的左右孩子
def checkHeapProperty(heap):
	size=heap.getSize()
	for parent in range(size):
		left=heap.getLeftChild(parent)
		right=heap.getRightChild(parent)
		if left<size:
			assert heap.items[parent]>=heap.items[left],(f"父节点 {heap.items[parent]} "
														 f"小于左孩子 {heap.items[left]}")
		if right<size:
			assert heap.items[parent]>=heap.items[right],(f"父节点 {heap.items[parent]} "
														  f"小于右孩子 {heap.items[right]}")


#测试空堆
def testEmptyHeap():
	heap=MaxHeap()
	assert heap.isEmpty()
	assert heap.getSize()==0
	assert heap.getPeek() is None
	assert heap.popItem() is None


#测试插入元素后堆顶、堆大小、元素完整性及堆结构是否正确
def testPushItem():
	heap=MaxHeap()
	values=[5,3,8,1,6,-2,4]
	for value in values:
		heap.pushItem(value)
		checkHeapProperty(heap)
	assert heap.getSize()==len(values)
	assert heap.getPeek()==max(values)
	assert sorted(heap.items)==sorted(values)


#测试连续删除堆顶后,返回结果是否按从大到小的顺序排列
def testPopItem():
	heap=MaxHeap()
	values=[7,2,9,1,5,3,-4,3]
	for value in values:
		heap.pushItem(value)
	result=[]
	while not heap.isEmpty():
		result.append(heap.popItem())
		checkHeapProperty(heap)
	assert result==sorted(values,reverse=True)
	assert heap.getSize()==0
	assert heap.isEmpty()


#测试只有一个元素时的插入、查看和删除操作
def testSingleItem():
	heap=MaxHeap()
	heap.pushItem(100)
	assert heap.getSize()==1
	assert heap.getPeek()==100
	assert heap.popItem()==100
	assert heap.isEmpty()
	assert heap.getPeek() is None
	assert heap.popItem() is None


#测试根据普通列表构造最大堆,并检查原列表是否保持不变
def testHeapify():
	heap=MaxHeap()
	values=[9,4,7,1,3,6,2]
	originalValues=values.copy()
	heap.heapify(values)
	checkHeapProperty(heap)
	assert heap.getSize()==len(values)
	assert heap.getPeek()==max(values)
	assert sorted(heap.items)==sorted(values)
	assert values==originalValues


#测试堆中包含重复元素时能否正确构造和依次弹出
def testDuplicateValues():
	heap=MaxHeap()
	values=[4,4,2,2,2,1,1,4]
	heap.heapify(values)
	checkHeapProperty(heap)
	result=[]
	while not heap.isEmpty():
		result.append(heap.popItem())
		checkHeapProperty(heap)
	assert result==sorted(values,reverse=True)


#测试堆中同时包含负数、零和正数时能否正常工作
def testNegativeValues():
	heap=MaxHeap()
	values=[-3,-10,5,0,-1,8,-10]
	for value in values:
		heap.pushItem(value)
		checkHeapProperty(heap)
	assert heap.getPeek()==8
	result=[]
	while not heap.isEmpty():
		result.append(heap.popItem())
	assert result==sorted(values,reverse=True)


#测试升序列表和降序列表构造最大堆后的弹出结果
def testSortedValues():
	testValues=[list(range(20)),list(range(20,0,-1))]
	for values in testValues:
		heap=MaxHeap()
		heap.heapify(values)
		checkHeapProperty(heap)
		result=[]
		while not heap.isEmpty():
			result.append(heap.popItem())
		assert result==sorted(values,reverse=True)


#测试使用较大的值替换堆顶后,旧值、堆顶、堆大小和堆结构是否正确
def testReplacePeekWithLargerValue():
	heap=MaxHeap()
	values=[8,4,7,2,6,3]
	heap.heapify(values)
	oldValue=heap.replacePeek(10)
	assert oldValue==8
	assert heap.getPeek()==10
	assert heap.getSize()==len(values)
	checkHeapProperty(heap)
	expectedValues=values.copy()
	expectedValues.remove(8)
	expectedValues.append(10)
	assert sorted(heap.items)==sorted(expectedValues)


#测试使用较小的值替换堆顶后,旧值、新堆顶和堆结构是否正确
def testReplacePeekWithSmallerValue():
	heap=MaxHeap()
	values=[9,7,8,3,5,4]
	heap.heapify(values)
	oldValue=heap.replacePeek(-10)
	assert oldValue==9
	checkHeapProperty(heap)
	expectedValues=values.copy()
	expectedValues.remove(9)
	expectedValues.append(-10)
	assert sorted(heap.items)==sorted(expectedValues)
	assert heap.getPeek()==8


#测试空堆调用replacePeek后能否正确插入新值
def testReplacePeekOnEmptyHeap():
	heap=MaxHeap()
	oldValue=heap.replacePeek(50)
	assert oldValue is None
	assert heap.getSize()==1
	assert heap.getPeek()==50
	checkHeapProperty(heap)


#将自定义最大堆与Python的heapq执行一万次随机操作并比较结果
def testRandomOperationsAgainstHeapq():
	randomGenerator=random.Random(2026)
	myHeap=MaxHeap()
	standardHeap=[]
	for _ in range(10000):
		shouldPush=(len(standardHeap)==0 or randomGenerator.random()<0.6)
		if shouldPush:
			value=randomGenerator.randint(-10000,10000)
			myHeap.pushItem(value)
			heapq.heappush(standardHeap,-value)
		else:
			myResult=myHeap.popItem()
			standardResult=-heapq.heappop(standardHeap)
			assert myResult==standardResult,(f"弹出结果不一致："
											 f"自定义堆返回 {myResult}，"
											 f"标准堆返回 {standardResult}")
		assert myHeap.getSize()==len(standardHeap)
		if standardHeap:
			assert myHeap.getPeek()==-standardHeap[0]
		else:
			assert myHeap.getPeek() is None
		checkHeapProperty(myHeap)
	while standardHeap:
		myResult=myHeap.popItem()
		standardResult=-heapq.heappop(standardHeap)
		assert myResult==standardResult
		checkHeapProperty(myHeap)
	assert myHeap.isEmpty()
