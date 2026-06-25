#二叉搜索树:任意节点中左节点值<当前节点值<右节点值,不允许值重复,不允许保存None

class TreeNode:
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class BinarySearchTree:
	def __init__(self):
		self.root=None
		self.size=0

	#插入值为value的节点
	def insertNode(self,value):
		#树为空,新节点为根节点
		if self.root is None:
			self.root=TreeNode(value)
			self.size+=1
			return True
		#树不为空,遍历树
		current=self.root
		while True:
			#新节点插入到左子树
			if value<current.value:
				#如果左节点为空,新节点作为新的左节点,结束遍历
				if current.left is None:
					current.left=TreeNode(value)
					self.size+=1
					return True
				#否则左节点不为空,当前节点指向左节点继续往左边遍历
				current=current.left
			#新节点插入到右子树
			elif value>current.value:
				#如果右节点为空,新节点作为新的右节点,结束遍历
				if current.right is None:
					current.right=TreeNode(value)
					self.size+=1
					return True
				#否则右节点不为空,当前节点指向右节点继续往右遍历
				current=current.right
			#存在值为value的节点,返回False
			else:
				return False

	#按值查找节点
	def findNode(self,value):
		current=self.root
		#从根节点开始遍历树
		while current is not None:
			#往左边遍历
			if value<current.value:
				current=current.left
			#往右边遍历
			elif value>current.value:
				current=current.right
			else:
				return current
		#退出循环或者根节点不存在,返回None
		return None

	#判断是否包含值为value的节点
	def containsNode(self,value):
		return self.findNode(value) is not None

	#获取最小节点值
	def getMinValue(self):
		if self.root is None:
			return None
		current=self.root
		#从根节点开始往左边遍历
		while current.left is not None:
			current=current.left
		return current.value

	#获取最大节点值
	def getMaxValue(self):
		if self.root is None:
			return None
		current=self.root
		#从根节点开始往右边遍历
		while current.right is not None:
			current=current.right
		return current.value

	#按照中序遍历的逻辑,查找目标节点值的后继节点值
	def successor(self,value):
		#查找树中值为value的节点
		node=self.findNode(value)
		if node is None:
			return None
		#目标节点存在且右子树存在,从右子树的左节点一直往下找(二叉搜索树的构造逻辑)
		if node.right is not None:
			current=node.right
			while current.left is not None:
				current=current.left
			return current.value
		#右子树不存在,从根节点开始
		successor=None
		current=self.root
		while current is not None:
			#当前节点值>目标节点,有可能是目标节点的后继节点,保存节点值
			if value<current.value:
				successor=current.value
				#当前节点的左子树可能存在一个>目标节点且<当前节点的节点,所以需要往左边遍历
				current=current.left
			#当前节点值<value,当前节点指向右子树
			elif value>current.value:
				current=current.right
			else:
				break
		#最后的successor保存的是所有比value大的祖先中,最小的那个
		return successor

	#
	def predecessor(self,value):
		node=self.findNode(value)
		if node is None:
			return None
		#
		if node.left is not None:
			current=node.left
			while current.right is not None:
				current=current.right
			return current.value
		#
		predecessor=None
		current=self.root
		while current is not None:
			if value>current.value:
				predecessor=current.value
				current=current.right
			elif value<current.value:
				current=current.left
			else:
				break
		return predecessor

	#按值删除节点
	def removeNode(self,value):
		self.root,flag=self.__removeNode__(self.root,value)
		if flag:
			self.size-=1
		return flag

	def __removeNode__(self,node,value):
		#根节点为空,删除失败返回Falese
		if node is None:
			return None,False
		#往左边遍历
		if value<node.value:
			node.left,flag=self.__removeNode__(node.left,value)
			return node,flag
		#往右边遍历
		elif value>node.value:
			node.right,flag=self.__removeNode__(node.right,value)
			return node,flag
		#当前节点值就是value
		else:
			if node.left is None:
				return node.right,True
			if node.right is None:
				return node.left,True
			successor=node.right
			while successor.left is not None:
				successor=successor.left
			node.value=successor.value
			node.right,temp=self.__removeNode__(node.right,successor.value)
			return node,True

	#前序遍历:根-左-右
	def preOrder(self):
		result=[]
		self.__preOrder__(self.root,result)
		return result

	def __preOrder__(self,node,result):
		if node is None:
			return
		result.append(node.value)
		self.__preOrder__(node.left,result)
		self.__preOrder__(node.right,result)

	#中序遍历:左-根-右
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

	#后序遍历:左-右-根
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

	#层序遍历:从上到下、从左到右
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
		return max(self.__getHeight__(node.left),self.__getHeight__(node.right))+1

	#判断二叉搜索树是否合法
	def isValid(self):
		return self.__isValid__(self.root,None,None)

	def __isValid__(self,node,low,high):
		if node is None:
			return True
		if low is not None and node.value<=low:
			return False
		if high is not None and node.value>=high:
			return False
		return (self.__isValid__(node.left,low,node.value)
				and self.__isValid__(node.right,node.value,high))

	#判断二叉搜索树是否为空
	def isEmpty(self):
		return self.root is None

	#
	def getSize(self):
		return self.size

	#输出二叉搜索树
	def show(self):
		self.__show__(self.root,0)
	def __show__(self,node,level):
		if node is None:
			return
		self.__show__(node.right,level+1)
		print("  "*level+str(node.value))
		self.__show__(node.left,level+1)

	#清空二叉搜索树
	def clear(self):
		self.root=None
		self.size=0
