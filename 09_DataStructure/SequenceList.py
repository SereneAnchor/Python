#顺序表

class SequenceList:
	#使用列表来存储顺序表元素
	def __init__(self):
		self.items=[]

	#在顺序表末尾添加值为value的元素(extend方法也可以)
	def appendItem(self,value):
		self.items.append(value)

	#在顺序表索引为index的位置插入值为value的元素
	def insertItem(self,index,value):
		self.items.insert(index,value)

	#移除顺序表中值为value的元素(若存在多个则移除第一个出现的元素、不存在报异常)
	def removeItem(self,value):
		if value not in self.items:
			raise ValueError(f"{value}不存在,无法删除.")
		self.items.remove(value)

	#修改索引为index位置处的元素值为value
	def modifyItem(self,index,value):
		self.items[index]=value

	#获取索引为index位置处的元素值
	def getItem(self,index):
		return self.items[index]

	#查找表中是否存在值为value的元素(存在返回其下标、否则返回-1)
	def findItem(self,value):
		if value in self.items:
			return self.items.index(value)
		return -1

	#获取顺序表长度
	def getLength(self):
		return len(self.items)

	#判断顺序表是否为空
	def isEmpty(self):
		return len(self.items)==0

	#输出顺序表(无return时默认返回None)
	def printList(self):
		print(f"输出顺序表:{self.items}")

if __name__=="__main__":
	#创建顺序表,表中无任何元素
	sequenceList=SequenceList()
	print(f"顺序表为空:{sequenceList.isEmpty()}")

	#往表中加入元素
	sequenceList.appendItem('A')
	sequenceList.appendItem('B')
	sequenceList.appendItem('C')
	sequenceList.printList()

	#在表中索引为1的位置插入'P'
	sequenceList.insertItem(1,'P')

	#修改表中索引为2的元素值为'X'
	sequenceList.modifyItem(2,'X')

	print(f"按索引[0]查找元素:{sequenceList.getItem(0)}")
	print(f"按元素'X'查找索引:{sequenceList.findItem('X')}")

	sequenceList.printList()
	print(f"顺序表长度:{sequenceList.getLength()}")


