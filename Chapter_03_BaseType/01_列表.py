#列表API

listA=['B','X','P','B','X','B']
print(f"列表A:{listA}")

#1.index:查询指定元素在列表中的下标,如果不存在直接报错
index=listA.index('P')
print(f"P的索引:{index}")

#2.count:统计指定元素在列表中出现的次数
count=listA.count('B')
print(f"B的数量:{count}")

#3.in、not in判断指定元素是否存在或不存在列表中
bool='W' in listA
print(f"W是否存在:{bool}")
bool='X' in listA
print(f"X是否存在:{bool}")

print(f"======== append ========")

#4.append:将指定元素增加到列表中
if 'G' not in listA:
	listA.append('G')
print(f"添加G到列表A:{listA}")

#5.extend:将列表B中的逐个元素追加到列表A中,适用于可迭代对象
listB=['R','S','T']
print(f"列表B:{listB}")
listA.extend(listB)
print(f"添加B到列表A:{listA}")

#6.insert:在指定索引处添加新元素,新元素通常是一个整体
listA.insert(0,'H')
print(f"索引0处插入H:{listA}")

print(f"======== delete ========")
#7.del:删除指定下标的元素
del listA[-4]
print(f"删除索引为-4的元素:{listA}")

#8.pop:删除指定下标的元素并返回被删除的元素(默认删除最后一个)
pop=listA.pop()
print(f"弹出索引为-1的元素:{pop}")
print(f"弹出后的列表A:{listA}")
pop=listA.pop(2)
print(f"弹出索引为2的元素:{pop}")
print(f"弹出后的列表A:{listA}")

#9.remove:移除列表中指定的元素(有多个则移除第一个出现的元素),如果不存在报错
listA.remove('H')
print(f"移除H的列表A:{listA}")

print(f"======== modify ========")
#10.修改某个索引的值
listA[-1]='A'
print(f"修改索引为-1的值:{listA}")

#11.reverse:反转列表
listA.reverse()
print(f"对列表A反转:{listA}")

#12.sort:reverse为True则反转,为False则不反转(先排序再根据reverse决定是否反转),默认为False升序
listA.sort(reverse=False)
print(f"从小到大排序:{listA}")
listA.sort(reverse=True)
print(f"从大到小排序:{listA}")

#列表嵌套:列表中的元素均由列表组成
list1=['小明','小红','小刚','小丽','小强']
list2=['小芳','小亮','小宇','小浩','小琪']
list3=['小诺','小泽','小琳','小航','小彤']
list4=[list1,list2,list3]

row=list4[1]
name=row[1]
print(f"姓名:{name}")

#for循环结束后,name指向'小彤',在循环外也能输出其值
for row in list4:
	for name in row:
		print(name,end='\t')
	print()

