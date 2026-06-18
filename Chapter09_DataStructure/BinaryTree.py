#二叉树

#树节点:每个节点包含自身节点值,指向左右节点的指针
class TreeNode:
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class BinaryTree:
	def __init__(self):
		self.root=None

	#判断二叉树是否为空
	def isEmpty(self):
		return self.root is None

	#
