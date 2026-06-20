import random

from Chapter09_DataStructure.BinaryTree import BinaryTree,TreeNode


#将树中的节点按层序转换为节点对象列表
def getLevelNodes(tree):
	if tree.root is None:
		return []
	nodes=[]
	queue=[tree.root]
	index=0
	while index<len(queue):
		current=queue[index]
		index+=1
		nodes.append(current)
		if current.left is not None:
			queue.append(current.left)
		if current.right is not None:
			queue.append(current.right)
	return nodes


#判断当前树的形状是否符合完全二叉树
def isCompleteBinaryTree(tree):
	if tree.root is None:
		return True
	queue=[tree.root]
	index=0
	foundEmptyPosition=False
	while index<len(queue):
		current=queue[index]
		index+=1
		if current is None:
			foundEmptyPosition=True
			continue
		if foundEmptyPosition:
			return False
		queue.append(current.left)
		queue.append(current.right)
	return True


#测试树节点的初始状态
def testTreeNode():
	node=TreeNode(10)
	assert node.value==10
	assert node.left is None
	assert node.right is None


#测试空二叉树的初始状态和各项结果
def testEmptyBinaryTree():
	tree=BinaryTree()
	assert tree.root is None
	assert tree.isEmpty()
	assert tree.findNode(1) is None
	assert not tree.containsNode(1)
	assert tree.preOrder()==[]
	assert tree.inOrder()==[]
	assert tree.postOrder()==[]
	assert tree.levelOrder()==[]
	assert tree.getHeight()==0
	assert tree.getNodeCount()==0
	assert tree.getLeafCount()==0
	assert tree.getMinValue() is None
	assert tree.getMaxValue() is None
	assert not tree.removeNode(1)


#测试插入第一个节点后是否成为根节点
def testInsertRootNode():
	tree=BinaryTree()
	tree.insertNode(10)
	assert tree.root is not None
	assert tree.root.value==10
	assert tree.root.left is None
	assert tree.root.right is None
	assert not tree.isEmpty()
	assert tree.levelOrder()==[10]


#测试连续插入节点后是否形成完全二叉树
def testInsertCompleteBinaryTree():
	tree=BinaryTree()
	for value in range(1,8):
		tree.insertNode(value)
	assert tree.levelOrder()==[1,2,3,4,5,6,7]
	assert tree.root.value==1
	assert tree.root.left.value==2
	assert tree.root.right.value==3
	assert tree.root.left.left.value==4
	assert tree.root.left.right.value==5
	assert tree.root.right.left.value==6
	assert tree.root.right.right.value==7
	assert isCompleteBinaryTree(tree)


#测试查找存在和不存在的节点
def testFindNode():
	tree=BinaryTree()
	for value in range(1,7):
		tree.insertNode(value)
	node=tree.findNode(5)
	assert isinstance(node,TreeNode)
	assert node.value==5
	assert tree.findNode(100) is None


#测试存在重复值时findNode是否返回层序遍历中第一个匹配节点
def testFindFirstDuplicateNode():
	tree=BinaryTree()
	for value in [1,2,2,3,4]:
		tree.insertNode(value)
	firstNode=tree.root.left
	secondNode=tree.root.right
	assert tree.findNode(2) is firstNode
	assert tree.findNode(2) is not secondNode


#测试containsValue是否能够正确判断节点值是否存在
def testContainsValue():
	tree=BinaryTree()
	for value in [10,20,30]:
		tree.insertNode(value)
	assert tree.containsNode(10)
	assert tree.containsNode(20)
	assert tree.containsNode(30)
	assert not tree.containsNode(40)


#测试前序、中序、后序和层序遍历结果
def testTraversalOrders():
	tree=BinaryTree()
	for value in range(1,7):
		tree.insertNode(value)
	assert tree.preOrder()==[1,2,4,5,3,6]
	assert tree.inOrder()==[4,2,5,1,6,3]
	assert tree.postOrder()==[4,5,2,6,3,1]
	assert tree.levelOrder()==[1,2,3,4,5,6]


#测试不同节点数量对应的二叉树高度
def testHeight():
	for nodeCount in range(0,100):
		tree=BinaryTree()
		for value in range(nodeCount):
			tree.insertNode(value)
		expectedHeight=nodeCount.bit_length()
		assert tree.getHeight()==expectedHeight


#测试高度计算是否适用于手动构造的非完全二叉树
def testHeightForSparseBinaryTree():
	tree=BinaryTree()
	tree.root=TreeNode(1)
	tree.root.right=TreeNode(2)
	tree.root.right.right=TreeNode(3)
	assert tree.getHeight()==3


#测试节点数量和叶子节点数量
def testNodeAndLeafCount():
	tree=BinaryTree()
	for value in range(1,7):
		tree.insertNode(value)
	assert tree.getNodeCount()==6
	assert tree.getLeafCount()==3
	assert tree.getHeight()==3


#测试最小值和最大值
def testMinAndMaxValue():
	tree=BinaryTree()
	for value in [8,-2,15,4,0,11]:
		tree.insertNode(value)
	assert tree.getMinValue()==-2
	assert tree.getMaxValue()==15


#测试从单节点树中删除根节点
def testRemoveOnlyRootNode():
	tree=BinaryTree()
	tree.insertNode(10)
	assert tree.removeNode(10)
	assert tree.root is None
	assert tree.isEmpty()
	assert not tree.removeNode(10)


#测试单节点树删除不存在的值时树保持不变
def testRemoveMissingValueFromSingleNodeTree():
	tree=BinaryTree()
	tree.insertNode(10)
	assert not tree.removeNode(20)
	assert tree.levelOrder()==[10]
	assert tree.getNodeCount()==1


#测试删除多节点树中不存在的值
def testRemoveMissingValue():
	tree=BinaryTree()
	for value in range(1,7):
		tree.insertNode(value)
	beforeValues=tree.levelOrder()
	assert not tree.removeNode(100)
	assert tree.levelOrder()==beforeValues
	assert tree.getNodeCount()==6


#测试删除根节点时是否使用最深最右节点的值覆盖
def testRemoveRootNode():
	tree=BinaryTree()
	for value in range(1,7):
		tree.insertNode(value)
	oldRoot=tree.root
	assert tree.removeNode(1)
	assert tree.root is oldRoot
	assert tree.levelOrder()==[6,2,3,4,5]
	assert tree.getNodeCount()==5
	assert isCompleteBinaryTree(tree)


#测试删除中间节点时是否保持完全二叉树
def testRemoveInternalNode():
	tree=BinaryTree()
	for value in range(1,7):
		tree.insertNode(value)
	targetNode=tree.findNode(2)
	assert tree.removeNode(2)
	assert targetNode.value==6
	assert tree.levelOrder()==[1,6,3,4,5]
	assert not tree.containsNode(2)
	assert tree.getNodeCount()==5
	assert isCompleteBinaryTree(tree)


#测试目标节点就是最深最右节点时能否正常删除
def testRemoveLastNode():
	tree=BinaryTree()
	for value in range(1,7):
		tree.insertNode(value)
	assert tree.removeNode(6)
	assert tree.levelOrder()==[1,2,3,4,5]
	assert tree.getNodeCount()==5
	assert isCompleteBinaryTree(tree)


#测试存在重复值时是否删除层序遍历中最后一个匹配节点
def testRemoveLastDuplicateNode():
	tree=BinaryTree()
	for value in [1,2,2,3,4]:
		tree.insertNode(value)
	firstDuplicate=tree.root.left
	assert tree.removeNode(2)
	assert tree.levelOrder()==[1,2,4,3]
	assert firstDuplicate.value==2
	assert tree.getNodeCount()==4
	assert isCompleteBinaryTree(tree)


#测试连续删除全部节点后树是否恢复为空树
def testRemoveAllNodes():
	tree=BinaryTree()
	for value in range(1,21):
		tree.insertNode(value)
	for value in range(1,21):
		assert tree.removeNode(value)
		assert isCompleteBinaryTree(tree)
	assert tree.isEmpty()
	assert tree.levelOrder()==[]
	assert tree.getNodeCount()==0


#测试清空二叉树
def testClearTree():
	tree=BinaryTree()
	for value in range(1,20):
		tree.insertNode(value)
	tree.clear()
	assert tree.root is None
	assert tree.isEmpty()
	assert tree.preOrder()==[]
	assert tree.inOrder()==[]
	assert tree.postOrder()==[]
	assert tree.levelOrder()==[]
	assert tree.getHeight()==0
	assert tree.getNodeCount()==0
	assert tree.getLeafCount()==0


#将二叉树与层序列表执行三千次随机操作并比较结果
def testRandomOperationsAgainstList():
	randomGenerator=random.Random(2026)
	tree=BinaryTree()
	values=[]
	for _ in range(3000):
		operation=randomGenerator.randint(0,4)
		value=randomGenerator.randint(-50,50)
		if operation<=1:
			tree.insertNode(value)
			values.append(value)
		elif operation==2:
			if value in values:
				targetIndex=max(index for index,item in enumerate(values) if item==value)
				values[targetIndex]=values[-1]
				values.pop()
				expectedResult=True
			else:
				expectedResult=False
			assert tree.removeNode(value)==expectedResult
		elif operation==3:
			assert tree.containsNode(value)==(value in values)
			node=tree.findNode(value)
			if value in values:
				assert node is not None
				assert node.value==value
			else:
				assert node is None
		else:
			if randomGenerator.random()<0.03:
				tree.clear()
				values.clear()

		assert tree.levelOrder()==values
		assert tree.getNodeCount()==len(values)
		assert tree.isEmpty()==(len(values)==0)
		assert tree.getHeight()==len(values).bit_length()
		expectedLeafCount=0 if len(values)==0 else (len(values)+1)//2
		assert tree.getLeafCount()==expectedLeafCount
		assert tree.getMinValue()==(min(values) if values else None)
		assert tree.getMaxValue()==(max(values) if values else None)
		assert isCompleteBinaryTree(tree)
