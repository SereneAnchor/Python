#案例1:计算嵌套元组中元素之和
tuple1=(1,3,5)
tuple2=(2,4,6)
tuple3=(9,8,7)
randomTuple=(tuple1,tuple2,tuple3)
sum=0
for row in randomTuple:
	for col in row:
		sum=sum+col
print(f"sum:{sum}")

#案例2:给定一个元组,将其中>5的数字放到新列表中
randomTuple=(2,3,4,5,6,7,8,9)
resultList=[]
for i in randomTuple:
	if i>5:
		resultList.append(i)
print(f"resultList:{resultList}")

