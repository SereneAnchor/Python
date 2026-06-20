#最小堆:父节点<=子节点

class MinHeap:

	#使用列表来存储堆元素
	def __init__(self):
		self.items=[]

	#获取当前节点的父节点(向下取整://、取余:%、返回小数的除法:/)
	def getParent(self,index):
		return (index-1)//2

	#获取当前节点的左孩子
	def getLeftChild(self,index):
		return 2*index+1

	#获取当前节点的右孩子
	def getRightChild(self,index):
		return 2*index+2

	#向上调整:当前节点和父节点比较,找出较小值进行交换;继续往上找
	def shiftUp(self,index):
		while index>0:
			#找到当前节点的父节点
			parent=self.getParent(index)
			#当前节点<父节点,当前节点和父节点交换,index上移指向当前较小的节点
			if self.items[index]<self.items[parent]:
				self.items[index],self.items[parent]=self.items[parent],self.items[index]
				index=parent
			#当前节点>父节点,不需要交换,仍然保持最小堆结构
			else:
				break

	#向下调整:当前节点和左右子节点比较,找出较小节点并进行交换;继续往下找
	def shiftDown(self,index):
		while True:
			#small指向当前节点
			small=index
			#获取当前节点的左右节点
			left=self.getLeftChild(index)
			right=self.getRightChild(index)
			#左节点存在且左节点<当前节点,small指向左节点
			if left<len(self.items) and self.items[left]<self.items[small]:
				small=left
			#右节点存在且右节点<当前节点,small指向右节点
			if right<len(self.items) and self.items[right]<self.items[small]:
				small=right
			#small指向当前节点,无需交换
			if small==index:
				break
			#交换当前节点和三者中较小的节点
			self.items[index],self.items[small]=self.items[small],self.items[index]
			#index下移指向当前较小的节点
			index=small

	#数组尾部插入元素,新元素在length-1的位置,树向上调整
	def pushItem(self,value):
		self.items.append(value)
		self.shiftUp(len(self.items)-1)

	#删除并返回堆顶元素(堆顶为最小值)
	def popItem(self):
		if self.isEmpty():
			return None
		#保存堆顶元素
		top=self.items[0]
		#移除数组最后一个元素(树中右下角的元素)
		last=self.items.pop()
		#移除后堆为空说明堆里只有一个元素,不向下继续执行;否则堆内至少还有一个元素
		if not self.isEmpty():
			#用最后一个元素替代堆顶
			self.items[0]=last
			#向下调整堆
			self.shiftDown(0)
		return top

	#获取堆顶元素不删除
	def getPeek(self):
		if self.isEmpty():
			return None
		return self.items[0]

	#根据给定的列表原地构造最小堆
	def heapify(self,values):
		self.items=list(values)
		for i in range(len(self.items)//2-1,-1,-1):
			self.shiftDown(i)

	#替换堆顶元素并返回原值
	def replacePeek(self,value):
		#堆为空直接插入value
		if self.isEmpty():
			self.items.append(value)
			return None
		#保存旧堆顶
		old=self.items[0]
		#将value放到堆顶
		self.items[0]=value
		#value的加入可能会破坏堆结构,所以需要向下调整
		self.shiftDown(0)
		return old

	#判断堆是否为空
	def isEmpty(self):
		return len(self.items)==0

	#获取堆的大小
	def getSize(self):
		return len(self.items)

	#以数组形式输出堆
	def show(self):
		print(self.items)

	#以树的形式输出堆
	def showTree(self,index=0,level=0):
		if index>=len(self.items):
			return
		self.showTree(self.getRightChild(index),level+1)
		print("  "*level+str(self.items[index]))
		self.showTree(self.getLeftChild(index),level+1)
