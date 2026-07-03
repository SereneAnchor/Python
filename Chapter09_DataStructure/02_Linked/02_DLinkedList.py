#双链表

#双链表节点
class Node:
	#每个节点包含数据域、前向域、后向域
	def __init__(self,value):
		self.value=value
		self.pre=None
		self.next=None

class DLinkedList:
	def __init__(self):
		self.head=None
		self.tail=None
		self.length=0

	#双链表尾部插入新节点
	def appendNode(self,value):
		newNode=Node(value)
		#双链表为空,头尾指针都指向该新节点
		if self.head is None:
			self.head=newNode
			self.tail=newNode
		#双链表中至少有一个节点:tail后域指向newNode,newNode前域指向tail,tail移动到新的尾结点
		else:
			self.tail.next=newNode
			newNode.pre=self.tail
			self.tail=newNode
		self.length+=1

	#双链表头部插入新节点
	def prependNode(self,value):
		newNode=Node(value)
		#双链表为空时头尾指针都指向该新节点
		if self.head is None:
			self.head=newNode
			self.tail=newNode
		#双链表中至少有一个节点:newNode后域指向head,head前域指向newNode,head移动到新的头节点
		else:
			newNode.next=self.head
			self.head.pre=newNode
			self.head=newNode
		self.length+=1

	#按值查找节点
	def findNode(self,value):
		current=self.head
		#双链表非空时遍历
		while current is not None:
			if current.value==value:
				return current
			current=current.next
		return None

	#判断表中是否包含值为value的节点
	def isContainsValue(self,value):
		return self.findNode(value) is not None

	#根据索引获取节点
	def getNode(self,index):
		if index<0 or index>=self.length:
			raise IndexError("Index out of range.")
		#索引落在表的前半段,从头节点开始遍历获取
		if index<self.length//2:
			current=self.head
			for i in range(index):
				current=current.next
		#索引落在表的后半段,从尾结点开始遍历获取
		else:
			current=self.tail
			for i in range(self.length-1-index):
				current=current.pre
		return current

	#根据索引获取节点的值
	def getNodeValue(self,index):
		return self.getNode(index).value

	#将索引为index的节点值改为value
	def modifyNodeValue(self,index,value):
		self.getNode(index).value=value

	#在目标值节点之后插入新节点
	def insertAfterNode(self,targetValue,newValue):
		#根据targetValue找到targetNode
		targetNode=self.findNode(targetValue)
		#若没有targetNode,即不能插入
		if targetNode is None:
			return False
		#若targetValue为尾结点,调用尾插法插入新节点
		if targetNode is self.tail:
			self.appendNode(newValue)
			return True
		#targetNode为非尾节点:targetNode->newNode->nextNode
		newNode=Node(newValue)
		nextNode=targetNode.next
		targetNode.next=newNode
		newNode.pre=targetNode
		newNode.next=nextNode
		nextNode.pre=newNode
		#双链表长度+1
		self.length+=1
		return True

	#在目标值节点之前插入新节点
	def insertBeforeNode(self,targetValue,newValue):
		#根据targetValue找到targetNode
		targetNode=self.findNode(targetValue)
		#若没有targetNode,即不能插入
		if targetNode is None:
			return False
		#若targetNode为头节点,调用头插法插入新节点
		if targetNode is self.head:
			self.prependNode(newValue)
			return True
		#targetNode为非头节点
		newNode=Node(newValue)
		preNode=targetNode.pre
		preNode.next=newNode
		newNode.pre=preNode
		newNode.next=targetNode
		targetNode.pre=newNode
		#双链表长度+1
		self.length+=1
		return True

	#移除头节点并返回值
	def popHead(self):
		if self.head is None:
			return None
		#保存头节点的value
		value=self.head.value
		#双链表中只有一个节点
		if self.head is self.tail:
			self.head=None
			self.tail=None
		#双链表中至少有两个节点
		else:
			self.head=self.head.next
			self.head.pre=None
		#双链表长度-1
		self.length-=1
		return value

	#移除尾结点并返回值
	def popTail(self):
		if self.tail is None:
			return None
		#保存尾节点的value
		value=self.tail.value
		#双链表中只有一个节点
		if self.head is self.tail:
			self.head=None
			self.tail=None
		#双链表中至少有两个节点
		else:
			self.tail=self.tail.pre
			self.tail.next=None
		#双链表长度-1
		self.length-=1
		return value

	#根据value移除节点
	def removeNode(self,value):
		#找到目标节点
		targetNode=self.findNode(value)
		if targetNode is None:
			return False
		#目标节点为头节点时采用头删法
		if targetNode is self.head:
			self.popHead()
			return True
		#目标节点为尾节点时采用尾删法
		if targetNode is self.tail:
			self.popTail()
			return True
		#目标节点为中间节点
		preNode=targetNode.pre
		nextNode=targetNode.next
		#断开目标节点
		preNode.next=nextNode
		nextNode.pre=preNode
		#双链表长度-1
		self.length-=1
		return True

	#获取双链表长度
	def getLength(self):
		return self.length

	#判断双链表是否为空
	def isEmpty(self):
		return self.length==0

	#清空双链表
	def clearList(self):
		self.head=None
		self.tail=None
		self.length=0

	#从头节点向后遍历并返回节点值列表
	def forwardToValue(self):
		values=[]
		current=self.head
		while current is not None:
			values.append(current.value)
			current=current.next
		return values

	#从尾节点向前遍历并返回节点值列表
	def backwardToValue(self):
		#使用列表保存各个节点的value
		values=[]
		current=self.tail
		while current is not None:
			values.append(current.value)
			current=current.pre
		return values

	#前向输出双链表
	def forwardPrintList(self):
		print(f"前向输出:{self.forwardToValue()}")

	#反向输出双链表
	def backwardPrintList(self):
		print(f"反向输出:{self.backwardToValue()}")
