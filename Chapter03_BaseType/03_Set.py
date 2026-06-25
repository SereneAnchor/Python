#Set:使用'{}'或者set方法定义集合,如果定义空集合,只能使用set方法

#定义有值集合:去重+输出无序(创建集合时会把每一个元素依次放进去,若存在已有元素就不再插入)
set1={'Serene','Anchor','Lumine','Ethere','Zenith','Serene'}
print(f"set1:{set1}")
print(f"set1 type:{type(set1)}")

#定义空集合:实际上是空的字典
set2=set()
print(f"set2 type:{type(set2)}")

#遍历集合
for ele in set1:
	print(ele,end="\t")
print()

#集合API
set3={'A','S','X','P'}

#1.add:向集合中增加一个元素
set3.add('B')
print(f"add B:{set3}")

#2.remove:删除集合中指定的数据,如果不存在则报错
set3.remove('A')
print(f"remove A:{set3}")

#3.in/not in:判断元素是否在集合中,存在返回True否则返回False
bool='Y' in set3
print(f"exist Y:{bool}")
bool='P' not in set3
print(f"not exist P:{bool}")
