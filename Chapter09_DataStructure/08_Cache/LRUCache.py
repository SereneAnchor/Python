#LRUCache:最近最少使用缓存,哈希表+双向链表

class CacheNode:
	#缓存节点包括:数据的键、数据的值、指向前后节点的指针
	def __init__(self,key=None,value=None):
		self.key=key
		self.value=value
		self.pre=None
		self.next=None

class LRUCache:
	#管理最大容量、根据key快速找到节点的字典、双向链表的虚拟头尾节点
	def __init__(self,capacity=8):
		self.capacity=capacity
		self.cache={}
		self.head=CacheNode()
		self.tail=CacheNode()
		self.head.next=self.tail
		self.tail.pre=self.head

	#
	def removeNode(self,node):
		node.pre.next=node.next
		node.next.pre=node.pre

	#
	def addToHead(self,node):
		node.next=self.head.next
		node.pre=self.head
		self.head.next.pre=node
		self.head.next=node

	#
	def moveToHead(self,node):
		self.removeNode(node)
		self.addToHead(node)

	#
	def popTail(self):
		node=self.tail.pre
		self.removeNode(node)
		return node

	#
	def get(self,key):
		if key not in self.cache:
			return None
		node=self.cache[key]
		self.moveToHead(node)
		return node.value

	#
	def put(self,key,value):
		#
		if key in self.cache:
			node=self.cache[key]
			node.value=value
			self.moveToHead(node)
			return
		#
		if len(self.cache)>=self.capacity:
			pop=self.popTail()
			del self.cache[pop.key]
		#
		node=CacheNode(key,value)
		self.cache[key]=node
		self.addToHead(node)

	#
	def remove(self,key):
		if key not in self.cache:
			return False
		node=self.cache[key]
		self.removeNode(node)
		del self.cache[key]
		return True

	#
	def containsKey(self,key):
		return key in self.cache

	#
	def isEmpty(self):
		return len(self.cache)==0

	#
	def isFull(self):
		return len(self.cache)==self.capacity

	#
	def getSize(self):
		return len(self.cache)

	#
	def getKeys(self):
		keys=[]
		current=self.head.next
		while current is not self.tail:
			keys.append(current.key)
			current=current.next
		return keys

	#
	def getValues(self):
		values=[]
		current=self.head.next
		while current is not self.tail:
			values.append(current.value)
			current=current.next
		return values

	#
	def show(self):
		pairs=[]
		current=self.head.next
		while current is not self.tail:
			pairs.append(f"{current.key}:{current.value}")
			current=current.next
		print(f"MRU [{','.join(pairs)}] LRU")

	#
	def clear(self):
		self.cache.clear()
		self.head.next=self.tail
		self.tail.pre=self.head