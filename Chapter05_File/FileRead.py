#1.一次性读取全部内容(适用于读取小文件,大文件会占用大量内存)
with open('Read.txt','r',encoding='utf-8') as file:
	#read方法返回所有内容的字符串形式(包括文件内部的换行)
	content=file.read()
print(content)

#2.逐行读取(适用于逐行处理,内存占用少)
with open('Read.txt','r',encoding='utf-8') as file:
	#先读一行,当前行非空就打印,并读取下一行(rstrip作用为去除读取的换行符)
	line=file.readline()
	while line:
		print(line.rstrip('\n'))
		line=file.readline()

#3.读取所有行到列表(适用于随机访问行,读取大文件时会占用内存)
with open('Read.txt','r',encoding='utf-8') as file:
	#一次性读取文件所有行,每一行作为列表中的一个元素
	lines=file.readlines()
	#enumerate作用为给列表每个元素配上编号,编号默认从0开始
	for i,line in enumerate(lines):
		print(f"第{i+1}行:{line.rstrip()}")

#4.迭代读取(内存效率最高,代码最简洁)
with open('Read.txt','r',encoding='utf-8') as file:
	#把文件对象file当成一个可迭代对象,通过for循环逐行读取
	for line in file:
		print(line.rstrip('\n'))

#5.处理大文件:分块读取(每次读取1024各字符)
def chunkByLargeFile(fileName,chunkSize=1024):
	with open(fileName,'r',encoding='utf-8') as file:
		while True:
			#从文件当前位置,读取1024个字符
			chunk=file.read(chunkSize)
			#chunk有内容,not chunk为假;chunk无内容,not chunk为真
			if not chunk:
				break
			printChunk(chunk)

def printChunk(chunk):
	print(chunk)

chunkByLargeFile('Read.txt')

#6.处理大文件:按行分块读取(每1000行打包为一组进行处理)
def lineByLargeFile(fileName,batchSize=1000):
	batch=[]
	with open(fileName,'r',encoding='utf-8') as file:
		for line in file:
			#去除字符串末尾的换行符加入到列表中
			batch.append(line.rstrip('\n'))
			if len(batch)==batchSize:
				printBatch(batch)
				batch=[]
		#处理最后不满足1024行的数据,如剩下5行,但是这5行在for循环内部不会做处理
		if batch:
			printBatch(batch)

def printBatch(batch):
	print(batch)

lineByLargeFile('Read.txt')