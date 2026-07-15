from collections import deque

class DirectedGraph:
	def __init__(self):
		self.adjList={}

	#
	def addVertex(self,vertex):
		if vertex not in self.adjList:
			self.adjList[vertex]=[]

	#
	def addEdge(self,fromVertex,toVertex):
		self.addVertex(fromVertex)
		self.addVertex(toVertex)
		#
		if toVertex not in self.adjList[fromVertex]:
			self.adjList[fromVertex].append(toVertex)

	#
	def removeVertex(self,vertex):
		if vertex not in self.adjList:
			return False
		for neighbors in self.adjList.values():
			if vertex in neighbors:
				neighbors.remove(vertex)
		del self.adjList[vertex]
		return True

	#
	def removeEdge(self,fromVertex,toVertex):
		if fromVertex not in self.adjList:
			return False
		if toVertex not in self.adjList[fromVertex]:
			return False
		self.adjList[fromVertex].remove(toVertex)
		return True

	#
	def getVertices(self):
		return list(self.adjList.keys())

	#
	def getEdges(self):
		edges=[]
		for u in self.adjList:
			for v in self.adjList[u]:
				edges.append((u,v))
		return edges

	#
	def getNeighbors(self,vertex):
		return self.adjList.get(vertex,[])

	#
	def getVertexCount(self):
		return len(self.adjList)

	#
	def getEdgeCount(self):
		return sum(len(neighbors) for neighbors in self.adjList.values())

	#
	def hasVertex(self,vertex):
		return vertex in self.adjList

	#
	def hasEdge(self,fromVertex,toVertex):
		if fromVertex not in self.adjList:
			return False
		return toVertex in self.adjList[fromVertex]

	#
	def inDegree(self,vertex):
		if vertex not in self.adjList:
			return None
		count=0
		for neighbors in self.adjList.values():
			if vertex in neighbors:
				count+=1
		return count

	#
	def topologicalSort(self):
		indeg={}
		for v in self.adjList:
			indeg[v]=self.inDegree(v)
		queue=deque([v for v,degree in indeg.items() if degree==0])
		result=[]
		#
		while queue:
			u=queue.popleft()
			result.append(u)
			for v in self.adjList[u]:
				indeg[v]-=1
				if indeg[v]==0:
					queue.append(v)
		if len(result)!=len(self.adjList):
			return None
		return result

	#
	def isCyclic(self):
		if not self.adjList:
			return False
		WHITE,GRAY,BLACK=0,1,2
		color={v:WHITE for v in self.adjList}
		#
		def DFS(vertex):
			color[vertex]=GRAY
			for neighbor in self.adjList[vertex]:
				if color[neighbor]==GRAY:
					return True
				if color[neighbor]==WHITE and DFS(neighbor):
					return True
			color[vertex]=BLACK
			return False
		#
		for vertex in self.adjList:
			if color[vertex]==WHITE:
				if DFS(vertex):
					return True
		return False

	#
	def BFS(self,start):
		if start not in self.adjList:
			return []
		visited={start}
		result=[start]
		queue=deque([start])
		#
		while queue:
			current=queue.popleft()
			for neighbor in self.adjList[current]:
				if neighbor not in visited:
					visited.add(neighbor)
					result.append(neighbor)
					queue.append(neighbor)
		return result

	#
	def show(self):
		for vertex in sorted(self.adjList.keys(),key=str):
			print(f"  {vertex}->{self.adjList[vertex]}")










