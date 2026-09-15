"""
	元组:与列表不同,它存储不可修改的数据(不允许通过赋值修改内容)
	元组内的数据也可以是不同的数据类型,只有单个元素时也需要添加','
"""

#元组API
tuple=(250,666,"SereneAnchor","王富贵",True,False,250)
print(f"元组:{tuple}")
print(f"索引为1的元素:{tuple[1]}")

#1.通过索引遍历元组(与遍历字符串、列表一样)
print(f"遍历元组:",end="")
for ele in tuple:
	print(ele,end=" ")
print()

#2.index:获取某个元素在元组中的索引
print(f"元素666的索引:{tuple.index(666)}")

#3.count:获取元素在元组中出现的次数
print(f"元素250的次数:{tuple.count(250)}")

#4.len:获取元组长度(元素个数)
print(f"元组长度:{len(tuple)}")
