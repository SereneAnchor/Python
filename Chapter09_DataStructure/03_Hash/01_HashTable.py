#哈希表

class HashTable:

	#构造哈希表
	def __init__(self,capacity=8):
		if not isinstance(capacity,int) or isinstance(capacity,bool) or capacity<=0:
			raise ValueError("哈希表容量必须是正整数!")
		#capacity表示桶数组容量,也就是一开始准备多少个桶
		self.capacity=capacity
		#buckets是哈希表真正存储数据的地方,一个大列表中的元素又是每一个小列表
		self.buckets=[ [] for _ in range(self.capacity)]
		#length表示哈希表真正保存了多少个键值对
		self.length=0

	#计算key所对应的hash值,一次运行时hash值不变
	def hash(self,key):
		#hash(key)会得到一个整数,取余之后能保证下标落在0到capacity-1之间
		return hash(key)%self.capacity

	#负载因子表示当前哈希表"装的有多满",负载因子越高,冲突通常越高,查找和删除可能变慢
	def loadFactor(self):
		#负载因子=已保存的键值对数量/桶数组容量
		return self.length/self.capacity

	#扩容(同一次程序运行时hash(key)不会变但是index可能会改变,因为修改了capacity)
	def resize(self):
		#扩容前先保存旧的键值对
		oldItems=self.getResults()
		#容量扩为原来的2倍
		self.capacity*=2
		#容量变了,hash(key)对capacity取余得到的index也可能变,必须重新创建数组
		self.buckets=[ [] for i in range(self.capacity)]
		#length必须赋为0,否则长度会重复累加;后续循环的setItem会重新计算length
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

	#将键值对存入桶中
	def setItem(self,key,value):
		#根据key计算它放在哪个桶里,bucket就是实际存放key-value的桶
		index=self.hash(key)
		bucket=self.buckets[index]
		#遍历桶,若key存在就更新value,pair是每一个键值对组合
		for pair in bucket:
			if pair[0]==key:
				pair[1]=value
				return
		#加入新键后负载因子超过0.75时先扩容
		if (self.length+1)/self.capacity>0.75:
			self.resize()
			#扩容后capacity发生变化,需要重新计算桶的位置
			index=self.hash(key)
			bucket=self.buckets[index]
		#把新的[key,value]放进这个桶
		bucket.append([key,value])
		self.length+=1

	#根据key找到桶返回对应的value
	def getItem(self,key,default=None):
		#根据key找到对应的桶
		index=self.hash(key)
		bucket=self.buckets[index]
		#在桶中逐个查找key;同一个桶里存在多个键值对,可能发生哈希冲突
		for pair in bucket:
			if pair[0]==key:
				return pair[1]
		#找不到key时返回调用者指定的默认值
		return default

	#判断某个key是否存在
	def containsKey(self,key):
		#无论key是否存在,一定能找到一个桶
		index=self.hash(key)
		bucket=self.buckets[index]
		#在某个桶内继续判断是否有key存在(桶为空或者是没有key)
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
			#bucket[i]表示第i个键值对
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
			#bucket内包含多个以list存储的键值对,取出每一个键值对
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
		#收集所有的键值对
		result=[]
		#bucket是每一个桶
		for bucket in self.buckets:
			#取出每一个桶中的各个键值对,以元组的形式添加到result中
			for key,value in bucket:
				result.append((key,value))
		return result

	#清空哈希表,但要保留当前capacity
	def clear(self):
		self.buckets=[ [] for i in range(self.capacity)]
		self.length=0

	#输出哈希表(enumerate返回一对值:下标+元素)
	def show(self):
		#输出每个桶的内容(桶的编号:桶的数据),观察哈希冲突和内部结构
		for index,bucket in enumerate(self.buckets):
			print(f"第{index}个桶{bucket}")

