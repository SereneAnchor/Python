#字典:存储人的信息,使用'{}',数据以键值对的形式存在,各个键值对以','相隔,键唯一且使用引号引起(类似于索引下标)

#定义有值字典
dict1={'姓名':'王富贵','性别':'male','年龄':20}
print(f"dict1:{dict1}")
for key in dict1:
	print(f"key:{key}",end=" ")
	print(f"value:{dict1[key]}")

#定义空字典
dict2={}
dict3=dict()

#dict[key]=value:如果key存在则修改对应的值,如果key不存在则新增该键值对

#字典API
person={'name':'张三','sex':'male','age':20,'num':250}

#1.del dict[key]:根据键删除键值对
del person['age']
print(f"person:{person}")

#2.clear:清除字典中的所有key
#person.clear()
print(f"person:{person}")

#3.根据键修改对应的值
person['num']=438
print(f"person:{person}")

#4.查询方法
#keys:以列表形式返回字典的所有key、values:以列表形式返回字典的所有值、items:以列表形式返回可遍历的键值对
list1=person.keys()
print(f"list1:{list1}")
list2=person.values()
print(f"list2:{list2}")
list3=person.items()
print(f"list3:{list3}")