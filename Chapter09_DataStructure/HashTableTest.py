from HashTable import HashTable

def runTest():
	#创建一个容量很小的哈希表,方便观察冲突和扩容
	table=HashTable(capacity=4)
	print("==========初始状态==========")
	print("是否为空:",table.isEmpty())
	print("长度:",table.getLength())
	table.printTable()

	#插入键值对
	print("\n==========插入数据==========")
	table.setItem("name","Tom")
	table.setItem("age",18)
	table.setItem("city","Beijing")
	print("长度:",table.getLength())
	table.printTable()

	#查询数据
	print("\n==========查询数据==========")
	print("name:",table.getItem("name"))
	print("age:",table.getItem("age"))
	print("不存在的key:",table.getItem("gender"))
	print("不存在的key,带默认值:",table.getItem("gender","不存在"))

	#更新已有 key
	print("\n==========更新数据==========")
	table.setItem("age",20)
	print("age:",table.getItem("age"))
	table.printTable()

	#制造哈希冲突:对整数来说,hash(1)%4、hash(5)%4、hash(9)%4 都会落到同一个桶
	print("\n==========哈希冲突==========")
	collisionTable=HashTable(capacity=4)
	collisionTable.setItem(1,"A")
	collisionTable.setItem(5,"B")
	collisionTable.setItem(9,"C")
	collisionTable.printTable()
	print("key 1:",collisionTable.getItem(1))
	print("key 5:",collisionTable.getItem(5))
	print("key 9:",collisionTable.getItem(9))

	#判断 key 是否存在
	print("\n==========判断 key 是否存在==========")
	print("是否包含name:",table.containsKey("name"))
	print("是否包含gender:",table.containsKey("gender"))

	#删除key
	print("\n==========删除数据==========")
	removedValue=table.removeItem("city")
	print("删除city,返回值:",removedValue)
	print("删除不存在的gender,返回值:",table.removeItem("gender"))
	table.printTable()

	#测试扩容
	print("\n==========测试扩容==========")
	resizeTable=HashTable(capacity=4)
	resizeTable.setItem("a",1)
	resizeTable.setItem("b",2)
	resizeTable.setItem("c",3)
	print("插入3个元素后,容量:",resizeTable.capacity)
	resizeTable.printTable()

	#这里再插入一个,负载因子达到条件,会触发扩容
	resizeTable.setItem("d",4)
	print("插入第4个元素后,容量:",resizeTable.capacity)
	resizeTable.printTable()

	#获取所有 key、value、键值对
	print("\n==========获取所有数据==========")
	print("keys:",resizeTable.getKeys())
	print("values:",resizeTable.getValues())
	print("items:",resizeTable.getResults())

	#清空表
	print("\n==========清空表==========")
	resizeTable.clearTable()
	print("是否为空:",resizeTable.isEmpty())
	print("长度:",resizeTable.getLength())
	resizeTable.printTable()


if __name__=="__main__":
	runTest()
