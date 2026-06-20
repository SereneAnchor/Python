#二叉树:通过层序插入构造完全二叉树,除最后一层外其余各层全部放满,最后一层节点从左到右连续排列

#树节点:每个节点包含自身节点值,指向左右节点的指针
class TreeNode:
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class BinaryTree:
	def __init__(self):
		self.root=None

	#判断二叉树是否为空,只需要检查根节点是否存在
	def isEmpty(self):
		return self.root is None

	#插入值为value的节点
	def insertNode(self,value):
		newNode=TreeNode(value)
		#如果为空树,那么新节点为根节点
		if self.root is None:
			self.root=newNode
			return
		#把根节点对象放入列表中
		queue=[self.root]
		index=0
		#进入while循环说明树中至少有一个节点(从上到下、从左到右的遍历)
		while index<len(queue):
			#取出列表中的第index个节点,index控制下一轮应该检查哪个节点
			current=queue[index]
			index+=1
			#从左节点开始,当前节点的左节点为空,新节点做为左节点,结束插入
			if current.left is None:
				current.left=newNode
				return
			#当前节点的左节点不为空,把左节点加入到节点列表中
			queue.append(current.left)
			#左节点不为空,当前节点的右节点为空,新节点作为右节点,结束插入
			if current.right is None:
				current.right=newNode
				return
			#当前节点的右节点不为空,把右节点加入到节点列表中
			queue.append(current.right)

	#按值查找节点
	def findNode(self,value):
		#根节点为空,二叉树为空树,返回None
		if self.root is None:
			return None
		queue=[self.root]
		index=0
		#进入while循环说明树中至少有一个节点
		while index<len(queue):
			current=queue[index]
			index+=1
			#判断当前节点值是否和value相等
			if current.value==value:
				return current
			#当前节点的左节点存在,将左节点添加到节点列表
			if current.left is not None:
				queue.append(current.left)
			#当前节点的右节点存在,将右节点添加到节点列表
			if current.right is not None:
				queue.append(current.right)
		#退出while循环说明没有找到值为value的节点
		return None

	#判断是否包含值为value的节点
	def containsNode(self,value):
		return self.findNode(value) is not None

	#对二叉树进行前序遍历:根-左-右
	def preOrder(self):
		#使用列表保存遍历过程中遇到的节点值
		result=[]
		self.__preOrder__(self.root,result)
		return result

	def __preOrder__(self,node,result):
		if node is None:
			return
		result.append(node.value)
		self.__preOrder__(node.left,result)
		self.__preOrder__(node.right,result)

	#对二叉树进行中序遍历:左-根-右
	def inOrder(self):
		result=[]
		self.__inOrder__(self.root,result)
		return result

	def __inOrder__(self,node,result):
		if node is None:
			return
		self.__inOrder__(node.left,result)
		result.append(node.value)
		self.__inOrder__(node.right,result)

	#对二叉树进行后序遍历:左-右-根
	def postOrder(self):
		result=[]
		self.__postOrder__(self.root,result)
		return result

	def __postOrder__(self,node,result):
		if node is None:
			return
		self.__postOrder__(node.left,result)
		self.__postOrder__(node.right,result)
		result.append(node.value)

	#对二叉树进行层序遍历:从上到下、从左到右
	def levelOrder(self):
		#使用列表保存遍历过程中遇到的节点值
		result=[]
		if self.root is None:
			return result
		queue=[self.root]
		index=0
		#进入while循环说明树中至少有一个节点
		while index<len(queue):
			current=queue[index]
			index+=1
			#先添加当前节点的value
			result.append(current.value)
			#当前节点的左节点存在,将左节点添加到节点列表
			if current.left is not None:
				queue.append(current.left)
			#当前节点的右节点存在,将右节点添加到节点列表
			if current.right is not None:
				queue.append(current.right)
		#返回一个保存各个节点值的列表
		return result

	#获取二叉树的高度
	def getHeight(self):
		return self.__getHeight__(self.root)

	def __getHeight__(self,node):
		if node is None:
			return 0
		leftHeight=self.__getHeight__(node.left)
		rightHeight=self.__getHeight__(node.right)
		return max(leftHeight,rightHeight)+1

	#获取二叉树节点数量
	def getNodeCount(self):
		return self.__getNodeCount__(self.root)

	def __getNodeCount__(self,node):
		if node is None:
			return 0
		return self.__getNodeCount__(node.left)+self.__getNodeCount__(node.right)+1

	#获取二叉树叶子节点数量
	def getLeafCount(self):
		return self.__getLeafCount__(self.root)

	def __getLeafCount__(self,node):
		if node is None:
			return 0
		#当前节点没有左节点和右节点
		if node.left is None and node.right is None:
			return 1
		return self.__getLeafCount__(node.left)+self.__getLeafCount__(node.right)

	#获取二叉树中最小节点值
	def getMinValue(self):
		values=self.levelOrder()
		if len(values)==0:
			return None
		return min(values)

	#获取二叉树中最大节点值
	def getMaxValue(self):
		values=self.levelOrder()
		if len(values)==0:
			return None
		return max(values)

	#按值删除节点:用最深最右节点的值覆盖目标节点,再断开最深最右节点,从而保持完全二叉树结构
	def removeNode(self,value):
		#空树移除失败,返回False
		if self.root is None:
			return False
		#树中只有根节点,判断根节点值与value是否相等
		if self.root.left is None and self.root.right is None:
			if self.root.value==value:
				self.root=None
				return True
			return False
		#targetNode保存目标节点,current遍历结束后指向最深最右节点,parentCurrent保存current的父节点
		targetNode=None
		current=None
		parentCurrent=None
		#使用列表保存(当前节点、当前节点的父节点),涉及到元组拆包
		queue=[(self.root,None)]
		index=0
		#进入while循环说明树中至少有两个节点,层序遍历整棵树,查找目标节点,同时让current最终指向最深最右节点
		while index<len(queue):
			current,parentCurrent=queue[index]
			index+=1
			#若存在重复值,targetNode最终保存层序遍历中最后一个匹配节点
			if current.value==value:
				targetNode=current
			#左节点不为空,将左节点、左节点的父节点加入节点列表
			if current.left is not None:
				queue.append((current.left,current))
			#右节点不为空,将右节点、右节点的父节点加入节点列表
			if current.right is not None:
				queue.append((current.right,current))
		#没有找到目标值的节点,返回False
		if targetNode is None:
			return False
		#否则就是找到了,用最深最右的节点值覆盖当前目标节点值
		targetNode.value=current.value
		#删除最深最右节点
		if parentCurrent.left is current:
			parentCurrent.left=None
		else:
			parentCurrent.right=None
		return True

	#清空二叉树
	def clear(self):
		self.root=None



