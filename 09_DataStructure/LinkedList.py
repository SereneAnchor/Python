#链表(None表示"没有对象")

#单链表节点
class Node:
	#每个节点包含数据域和指向下一个节点的指针域(创建的新节点没有连接到任何其它节点,所以next为None)
	def __init__(self,value):
		self.value=value
		self.next=None


class LinkedList:
	#head指向链表第一个节点(头节点),它本身不是节点,Node才创建真正的节点(head为None链表为空,否则指向第一个节点)
	def __init__(self):
		self.head=None

	#链表尾部插入新节点
	def appendNode(self,value):
		newNode=Node(value)
		#链表为空时让head指向newNode
		if self.head is None:
			self.head=newNode
			return
		#链表非空时(有1个节点或者多个节点),找到链表的最后一个节点,让最后一个节点的next指向newNode
		current=self.head
		while current.next is not None:
			current=current.next
		current.next=newNode

	#链表头部插入新节点(让新节点的next先指向head,head要么为空要么指向下一个节点,再让head指向新节点)
	def prependNode(self,value):
		newNode=Node(value)
		newNode.next=self.head
		self.head=newNode

	#按值查找节点
	def findNode(self,value):
		current=self.head
		#链表非空
		while current is not None:
			if current.value==value:
				return current
			current=current.next

	#按值删除节点(删除成功返回True、否则返回False)
	def removeNode(self,value):
		#头节点为空链表为空队列,返回False
		if self.head is None:
			return False
		#头节点非空优先判断该节点值是否为value
		if self.head.value==value:
			self.head=self.head.next
			return True
		#头节点值不是value,从头开始遍历链表
		previous=self.head
		current=self.head.next
		#进入循环说明链表中至少有两个节点
		while current is not None:
			if current.value==value:
				previous.next=current.next
				return True
			previous=current
			current=current.next
		return False

	#判断链表是否为空
	def isEmpty(self):
		return self.head is None

	#输出链表
	def printLinkedList(self):
		values=[]
		current=self.head
		#头节点不为空时,将每个节点的value值加入到列表中
		while current is not None:
			values.append(current.value)
			current=current.next
		print(f"输出链表:{values}")

if __name__=="__main__":
	#创建单链表
	linkedList=LinkedList()
	print(f"链表为空:{linkedList.isEmpty()}")

	#尾插元素
	linkedList.appendNode('A')
	linkedList.appendNode('B')
	linkedList.appendNode('C')
	linkedList.appendNode('D')
	linkedList.printLinkedList()

	#头插元素
	linkedList.prependNode('E')
	linkedList.printLinkedList()

	findNode=linkedList.findNode('X')
	if findNode is None:
		print(f"Find X:None.")
	else:
		print(f"Find X:{findNode.value}")

	print(f"Remove B:{linkedList.removeNode('B')}")
	linkedList.printLinkedList()

	print(f"Remove H:{linkedList.removeNode('H')}")
	linkedList.printLinkedList()




























