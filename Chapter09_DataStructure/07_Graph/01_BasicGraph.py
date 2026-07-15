from collections import deque

class BasicGraph:
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
			self.adjList[toVertex].append(fromVertex)

	#
	def removeVertex(self,vertex):
		if vertex not in self.adjList:
			return False
		for neighbor in self.adjList[vertex]:
			self.adjList[neighbor].remove(vertex)
		del self.adjList[vertex]
		return True

	#
	def removeEdge(self,fromVertex,toVertex):
		if fromVertex not in self.adjList:
			return False
		if toVertex not in self.adjList[fromVertex]:
			return False
		#
		self.adjList[fromVertex].remove(toVertex)
		self.adjList[toVertex].remove(fromVertex)
		return True

	#
	def getVertices(self):
		return len(self.adjList.keys())

	#
	def getEdges(self):
		edges=[]
		seen=set()
		for u in self.adjList:
			for v in self.adjList[u]:
				key=(min(u,v),max(u,v))
				if key not in seen:
					seen.add(key)
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
		total=0
		for neighbors in self.adjList.values():
			total+=len(neighbors)
		return total//2

	#
	def hasVertex(self,vertex):
		return vertex in self.adjList

	#
	def hasEdge(self,fromVertex,toVertex):
		if fromVertex not in self.adjList:
			return False
		return toVertex in self.adjList[fromVertex]

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
				visited.add(neighbor)
				result.append(neighbor)
				queue.append(neighbor)
		return result

	#
	def DFS(self,start):
		if start not in self.adjList:
			return []
		visited={start}
		result=[]
		stack=[start]
		#
		while stack:
			current=stack.pop()
			if current not in result:
				result.append(current)
			for neighbor in self.adjList[current]:
				if neighbor not in visited:
					visited.add(neighbor)
					stack.append(neighbor)
		return result

	#
	def hasPath(self,start,end):
		return end in self.BFS(start)

	#
	def show(self):
		for vertex in sorted(self.adjList.keys(),key=str):
			print(f"  {vertex}->{self.adjList[vertex]}")




