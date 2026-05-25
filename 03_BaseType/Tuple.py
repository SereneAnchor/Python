#元组:与列表不同,它存储不可修改的数据(不允许通过赋值修改内容)
#元组内的数据也可以是不同的数据类型,只有单个元素时也需要添加','

#元组API
tuple=(250,666,"SereneAnchor","王富贵",True,False,250)
print(f"tuple1:{tuple}")

#1.通过索引遍历元组(与遍历字符串、列表一样)
for ele in tuple:
	print(ele,end="\t")
print()

#2.index:获取某个元素在元组中的索引
print(f"index 666:{tuple.index(666)}")

#3.count:获取元素在元组中出现的次数
print(f"count 250:{tuple.count(250)}")

#4.len:获取元组长度
print(f"len(tuple):{len(tuple)}")
