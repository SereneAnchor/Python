#并查集

class UnionFind:
	#
	def __init__(self,count):
		self.parent=list(range(count))
		self.rank=[0]*count
		self.count=count

	#
	def find(self,x):
		if self.parent[x]!=x:
			self.parent[x]=self.find(self.parent[x])
		return self.parent[x]

	#
	def union(self,x,y):
		X=self.find(x)
		Y=self.find(y)
		if X==Y:
			return False
		if self.rank[X]<self.rank[Y]:
			self.parent[X]=Y
		elif self.rank[X]>self.rank[Y]:
			self.parent[Y]=X
		else:
			self.parent[Y]=X
			self.rank[X]+=1
		self.count-=1
		return True

	#
	def isConnected(self,x,y):
		return self.find(x)==self.find(y)

	#
	def getCount(self):
		return self.count

	#
	def getSize(self,x):
		root=self.find(x)
		size=0
		for i in range(len(self.parent)):
			if self.find(i)==root:
				size+=1
		return size

	#
	def getRoots(self):
		roots=[]
		for i in range(len(self.parent)):
			if self.parent[i]==i:
				roots.append(i)
		return roots

	#
	def getMembers(self,x):
		root=self.find(x)
		members=[]
		for i in range(len(self.parent)):
			if self.find(i)==root:
				members.append(i)
		return members

	#
	def getGroups(self):
		groups=[]
		for i in range(len(self.parent)):
			root=self.find(i)
			if root not in groups:
				groups[root]=[]
			groups[root].append(i)
		return groups

	#
	def printCollect(self):
		print(f"parent:{self.parent}")
		print(f"rank  :{self.rank}")
		print(f"Sets  :{self.count}")
