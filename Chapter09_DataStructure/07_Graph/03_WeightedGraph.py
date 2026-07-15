import heapq

class WeightedGraph:
	def __init__(self):
		self.adjList={}

	#
	def addVertex(self,vertex):
		if vertex not in self.adjList:
			self.adjList[vertex]=[]

	#
	def addEdge(self,fromVertex,toVertex,weight=1):
		self.addVertex(fromVertex)
		self.addVertex(toVertex)
		#
		for index,(neighbor,_) in enumerate(self.adjList[fromVertex]):
			if neighbor==toVertex:
				self.adjList[fromVertex][index]=(toVertex,weight)
				for i,(n,_) in enumerate(self.adjList[toVertex]):
					if n==fromVertex:
						self.adjList[toVertex][i]=(fromVertex,weight)
						break
				return
		self.adjList[fromVertex].append(toVertex,weight)
		self.adjList[toVertex].append(fromVertex,weight)

	#
	def removeVertex(self,vertex):
		if vertex not in self.adjList:
			return False

		for neighbor,_ in self.adjList[vertex]:
			self.adjList[neighbor]=[(v,w) for v,w in self.adjList[neighbor] if v!=vertex]
		del self.adjList[vertex]
		return True

	#
	def removeEdge(self,fromVertex,toVertex):
		if fromVertex not in self.adjList:
			return False
		if toVertex not in self.adjList:
			return False
		before=len(self.adjList[fromVertex])
		self.adjList[fromVertex]=[(v,w) for v,w in self.adjList[fromVertex] if v!=toVertex]
		if len(self.adjList[fromVertex])==before:
			return False
		self.adjList[toVertex]=[(v,w) for v,w in self.adjList[toVertex] if v!=fromVertex]
		return True

	#
	def getVertices(self):
		return list(self.adjList.keys())

	#
	def getEdges(self):
		edges=[]
		seen=set()
		for u in self.adjList:
			for v,w in self.adjList[u]:
				key=(min(u,v),max(u,v))
				if key not in seen:
					seen.add(key)
					edges.append((u,v,w))
		return edges

	#
	def getNeighbors(self,vertex):
		if vertex not in self.adjList:
			return []
		return [neighbor for neighbor,_ in self.adjList[vertex]]

	#
	def getWeight(self,fromVertex,toVertex):
		if fromVertex not in self.adjList:
			return None
		for neighbor,weight in self.adjList[fromVertex]:
			if neighbor==toVertex:
				return weight
		return None

	#
	def getVertexCount(self):
		return len(self.adjList)

	#
	def hasVertex(self,vertex):
		return vertex in self.adjList

	#
	def hasEdge(self,fromVertex,toVertex):
		if fromVertex not in self.adjList:
			return False
		return any(neighbor==toVertex for neighbor,_ in self.adjList[fromVertex])

	#
	def shortTestPath(self,start,end):
		if start not in self.adjList or end not in self.adjList:
			return None,None
		#
		distances={v:float("inf") for v in self.adjList}
		distances[start]=0
		previous={start:None}
		#
		heap=[(0,start)]
		visited=set()
		#
		while heap:
			currentDist,current=heapq.heappop(heap)
			#
			if current in visited:
				continue
			visited.add(current)
			#
			if current==end:
				break
			#
			for neighbor,weight in self.adjList[current]:
				if neighbor in visited:
					continue
				newDist=currentDist+weight
				if newDist<distances[neighbor]:
					distances[neighbor]=newDist
					previous[neighbor]=current
					heapq.heappush(heap,(newDist,neighbor))
		#
		if end not in previous or distances[end]==float("inf"):
			return None,None
		path=[]
		node=end
		while node is not None:
			path.append(node)
			node=previous[node]
		path.reverse()
		return distances[end],path

	#
	def show(self):
		for vertex in sorted(self.adjList.keys(),key=str):
			edges=",".join(f"{v}({w})" for v,w in self.adjList[vertex])
			print(f" {vertex}-[{edges}")











