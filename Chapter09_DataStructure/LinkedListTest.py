from LinkedList import LinkedList

def runTest():
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

if __name__=="__main__":
	runTest()