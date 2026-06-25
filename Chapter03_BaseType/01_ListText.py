import random

length=random.randint(2,10)
randomList=[random.randint(2,10) for i in range(length)]
#案例1:在一个随机整数数组中,判断相邻两个元素的大写关系,反映为'上升'/'下降'记录到另一个数组中
str1="上升"
str2="下降"
str3="相等"
resultList=[]
print(f"length:{length}")
print(f"randomList:{randomList}")
for i in range(length-1):
	if randomList[i]>randomList[i+1]:
		resultList.append(str2)
	elif randomList[i]<randomList[i+1]:
		resultList.append(str1)
	else:
		resultList.append(str3)
print(f"resultList:{resultList}")

#案例2:找出列表中第一次重复出现的元素并输出
countList=[]
for i in randomList:
	if i not in countList:
		countList.append(i)
	else:
		print(f"{i}")
		break