#哈希表

class HashTable:

	#
	def __init__(self,capacity=8):
		#capacity表示桶数组容量,也就是一开始准备多少个桶
		self.capacity=capacity
		#buckets是哈希表真正存储数据的地方,一个大列表中的元素又是每一个小列表
		self.buckets=[ [] for i in range(self.capacity)]
		#length表示哈希表真正保存了多少个键值对
		self.length=0

	#
	def hash(self,key):
		#hash(key)会得到一个整数,取余之后能保证下标落在0到capacity-1之间
		return hash(key)%self.capacity

	#负载因子表示当前哈希表"装的有多满",负载因子越高,冲突通常越高,查找和删除可能变慢
	def loadFactor(self):
		#负载因子=已保存的键值对数量/桶数组容量
		return self.length/self.capacity

	#扩容
	def resize(self):
		#扩容前先保存旧的键值对
		oldItems=self.getResults()
		#容量扩为原来的2倍
		self.capacity*=2
		#容量变了,key对capacity取余得到的index也可能变,必须重新创建数组
		self.buckets=[ [] for i in range(self.capacity)]
		self.length=0
		#把旧键值对重新插入新桶数组,重新计算每个key的位置(rehash)
		for key,value in oldItems:
			self.setItem(key,value)

	#判断哈希表是否为空,即无任何键值对
	def isEmpty(self):
		return self.length==0

	#获取哈希表长度,即键值对数量
	def getLength(self):
		return self.length

	#
	def setItem(self,key,value):
		#若负载因子过高,则先扩容减少后续冲突
		if self.loadFactor()>=0.75:
			self.resize()
		#根据key计算它放在哪个桶里
		index=self.hash(key)
		bucket=self.buckets[index]
		#若key存在就更新value
		for pair in bucket:
			if pair[0]==key:
				pair[1]=value
				return
		#key不存在就把新的[key,value]放进这个桶
		bucket.append([key,value])
		self.length+=1

	#
	def getItem(self,key,default=None):
		#根据key找到对应的桶
		index=self.hash(key)
		bucket=self.buckets[index]
		#在桶中逐个查找key;可能发生哈希冲突,同一个桶里存在多个键值对
		for pair in bucket:
			if pair[0]==key:
				return pair[1]
		#找不到key返回默认值None
		return default

	#判断某个key是否存在
	def containsKey(self,key):
		index=self.hash(key)
		bucket=self.buckets[index]
		for pair in bucket:
			if pair[0]==key:
				return True
		return False

	#根据key删除
	def removeItem(self,key):
		#根据key找到对应的桶
		index=self.hash(key)
		bucket=self.buckets[index]
		#遍历桶,找到key后删除整个[key,value]
		for i in range(len(bucket)):
			if bucket[i][0]==key:
				removedPair=bucket.pop(i)
				self.length-=1
				#删除成功时返回被删除的value,方便知道删除了什么
				return removedPair[1]
		#key不存在返回None
		return None

	#返回哈希表中所有key,类似于dict.keys()
	def getKeys(self):
		keys=[]
		for bucket in self.buckets:
			for key,value in bucket:
				keys.append(key)
		return keys

	#返回哈希表中所有value,类似于dict.values()
	def getValues(self):
		values=[]
		for bucket in self.buckets:
			for key,value in bucket:
				values.append(value)
		return values

	#返回哈希表中所有key、value,类似于dict.items()
	def getResults(self):
		result=[]
		for bucket in self.buckets:
			for key,value in bucket:
				result.append((key,value))
		return result

	#清空哈希表,但要保留当前capacity
	def clearTable(self):
		self.buckets=[ [] for i in range(self.capacity)]
		self.length=0

	#输出哈希表
	def printTable(self):
		#输出每个桶的内容,观察哈希冲突和内部结构
		for index,bucket in enumerate(self.buckets):
			print(f"{index}:{bucket}")

