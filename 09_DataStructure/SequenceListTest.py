from SequenceList import SequenceList

def runTest():
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

if __name__=="__main__":
	runTest()