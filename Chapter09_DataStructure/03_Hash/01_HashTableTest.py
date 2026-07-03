import random
from importlib import import_module
from pathlib import Path
import sys

import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[2]))

module=import_module("Chapter09_DataStructure.03_Hash.01_HashTable")
HashTable=module.HashTable


#构造具有相同哈希值的键,用于测试哈希冲突
class CollisionKey:
	def __init__(self,value):
		self.value=value

	def __hash__(self):
		return 1

	def __eq__(self,other):
		return isinstance(other,CollisionKey) and self.value==other.value


#测试非法初始容量是否会抛出异常
def testInvalidCapacity():
	invalidCapacities=[0,-1,1.5,"8",True,False,None]
	for capacity in invalidCapacities:
		with pytest.raises(ValueError,match="哈希表容量必须是正整数!"):
			HashTable(capacity)


#测试新建哈希表的初始状态是否正确
def testEmptyHashTable():
	hashTable=HashTable()
	assert hashTable.capacity==8
	assert hashTable.getLength()==0
	assert hashTable.isEmpty()
	assert hashTable.loadFactor()==0
	assert hashTable.getKeys()==[]
	assert hashTable.getValues()==[]
	assert hashTable.getResults()==[]


#测试插入键值对后查询、长度和判空结果是否正确
def testSetAndGetItem():
	hashTable=HashTable()
	hashTable.setItem("name","Alice")
	hashTable.setItem("age",20)
	assert hashTable.getItem("name")=="Alice"
	assert hashTable.getItem("age")==20
	assert hashTable.getLength()==2
	assert not hashTable.isEmpty()


#测试更新已有键时只修改值且不会增加长度或触发扩容
def testUpdateExistingKeyWithoutResize():
	hashTable=HashTable(4)
	hashTable.setItem(0,"a")
	hashTable.setItem(1,"b")
	hashTable.setItem(2,"c")
	assert hashTable.capacity==4
	assert hashTable.loadFactor()==0.75
	hashTable.setItem(1,"newValue")
	assert hashTable.getItem(1)=="newValue"
	assert hashTable.getLength()==3
	assert hashTable.capacity==4


#测试查询不存在的键时能否返回默认值
def testGetItemWithDefault():
	hashTable=HashTable()
	assert hashTable.getItem("missing") is None
	assert hashTable.getItem("missing","notFound")=="notFound"


#测试containsKey能否正确判断键是否存在
def testContainsKey():
	hashTable=HashTable()
	hashTable.setItem("name","Alice")
	assert hashTable.containsKey("name")
	assert not hashTable.containsKey("age")


#测试删除存在的键后返回值、长度和查询结果是否正确
def testRemoveItem():
	hashTable=HashTable()
	hashTable.setItem("name","Alice")
	hashTable.setItem("age",20)
	removedValue=hashTable.removeItem("name")
	assert removedValue=="Alice"
	assert not hashTable.containsKey("name")
	assert hashTable.getItem("name") is None
	assert hashTable.getLength()==1


#测试删除不存在的键时返回None且哈希表状态保持不变
def testRemoveMissingKey():
	hashTable=HashTable()
	hashTable.setItem("name","Alice")
	assert hashTable.removeItem("age") is None
	assert hashTable.getLength()==1
	assert hashTable.getItem("name")=="Alice"


#测试多个键发生哈希冲突时能否正确插入、查询、更新和删除
def testHashCollision():
	hashTable=HashTable()
	key1=CollisionKey("a")
	key2=CollisionKey("b")
	key3=CollisionKey("c")
	hashTable.setItem(key1,10)
	hashTable.setItem(key2,20)
	hashTable.setItem(key3,30)
	assert hashTable.getItem(key1)==10
	assert hashTable.getItem(key2)==20
	assert hashTable.getItem(key3)==30
	assert hashTable.getLength()==3
	hashTable.setItem(key2,200)
	assert hashTable.getItem(key2)==200
	assert hashTable.getLength()==3
	assert hashTable.removeItem(key1)==10
	assert not hashTable.containsKey(key1)
	assert hashTable.getItem(key2)==200
	assert hashTable.getItem(key3)==30


#测试加入新键后负载因子超过0.75时是否自动扩容并保留原有数据
def testResize():
	hashTable=HashTable(4)
	for key in range(3):
		hashTable.setItem(key,key*10)
	assert hashTable.capacity==4
	assert hashTable.loadFactor()==0.75
	hashTable.setItem(3,30)
	assert hashTable.capacity==8
	assert hashTable.getLength()==4
	assert hashTable.loadFactor()==0.5
	for key in range(4):
		assert hashTable.getItem(key)==key*10


#测试连续插入大量键值对时能否多次扩容并保留全部数据
def testMultipleResize():
	hashTable=HashTable(1)
	for key in range(100):
		hashTable.setItem(key,key*2)
	assert hashTable.capacity>=128
	assert hashTable.getLength()==100
	assert hashTable.loadFactor()<=0.75
	for key in range(100):
		assert hashTable.getItem(key)==key*2


#测试getKeys、getValues和getResults返回的数据是否完整
def testGetKeysValuesAndResults():
	hashTable=HashTable()
	data={"name":"Alice","age":20,"score":95}
	for key,value in data.items():
		hashTable.setItem(key,value)
	assert set(hashTable.getKeys())==set(data.keys())
	assert sorted(hashTable.getValues(),key=str)==sorted(data.values(),key=str)
	assert dict(hashTable.getResults())==data


#测试保存None值时能否通过containsKey区分键存在和键不存在
def testStoreNoneValue():
	hashTable=HashTable()
	hashTable.setItem("empty",None)
	assert hashTable.containsKey("empty")
	assert hashTable.getItem("empty") is None
	assert not hashTable.containsKey("missing")
	assert hashTable.getLength()==1


#测试清空哈希表后数据和长度归零且当前容量保持不变
def testClearTable():
	hashTable=HashTable(4)
	for key in range(10):
		hashTable.setItem(key,key)
	currentCapacity=hashTable.capacity
	hashTable.clear()
	assert hashTable.capacity==currentCapacity
	assert hashTable.getLength()==0
	assert hashTable.isEmpty()
	assert hashTable.getKeys()==[]
	assert hashTable.getValues()==[]
	assert hashTable.getResults()==[]
	assert all(bucket==[] for bucket in hashTable.buckets)


#测试输出哈希表时每个桶显示的内容是否正确
def testPrintTable(capsys):
	hashTable=HashTable(4)
	hashTable.setItem(0,"a")
	hashTable.setItem(4,"b")
	hashTable.show()
	output=capsys.readouterr().out
	expected=("第0个桶[[0, 'a'], [4, 'b']]\n"
			  "第1个桶[]\n"
			  "第2个桶[]\n"
			  "第3个桶[]\n")
	assert output==expected


#将自定义哈希表与Python字典执行一万次随机操作并比较结果
def testRandomOperationsAgainstDict():
	randomGenerator=random.Random(2026)
	myTable=HashTable(2)
	standardTable={}
	for _ in range(10000):
		operation=randomGenerator.randint(0,4)
		key=randomGenerator.randint(-200,200)
		if operation==0:
			value=randomGenerator.randint(-10000,10000)
			myTable.setItem(key,value)
			standardTable[key]=value
		elif operation==1:
			defaultValue="notFound"
			assert myTable.getItem(key,defaultValue)==standardTable.get(key,defaultValue)
		elif operation==2:
			assert myTable.containsKey(key)==(key in standardTable)
		elif operation==3:
			expectedValue=standardTable.pop(key,None)
			assert myTable.removeItem(key)==expectedValue
		else:
			if randomGenerator.random()<0.02:
				myTable.clear()
				standardTable.clear()
		assert myTable.getLength()==len(standardTable)
		assert myTable.isEmpty()==(len(standardTable)==0)
		assert dict(myTable.getResults())==standardTable
		assert set(myTable.getKeys())==set(standardTable.keys())
		assert sorted(myTable.getValues())==sorted(standardTable.values())
		assert myTable.loadFactor()<=0.75
