#列表和元组都可以通过len方法获取元素个数

#列表:在C++、Java中等价于数组,但可以存储不同类型的数据(整数、字符串、甚至是字典)
#索引:索引从0开始依次往后;也可以从-1开始依次往前

#列表的可变性
#1、原地修改元素:直接通过索引来修改列表中某个元素的值
list1=[10,20,30]
print(f"list1:{list1}",end="\t")
print(f"list1 address:{id(list1)}")
list1[2]=300
print(f"======== set list1[2]={300} ========")
print(f"list1:{list1}",end="\t")
print(f"list1 address:{id(list1)}")
print()

#2、动态增删:列表大小不固定,可以在其中任意添加和删除元素
list2=["Paper A","Paper B"]
print(f"list2:{list2}")
print(f"======== add {'Paper C'} to list2 ========")
list2.append("Paper C")
print(f"list2:{list2}")
print()

#3、内部状态灵活:元素可以是任何类型的对象
list3=['A','B','C']
list4=list3
print(f"list3:{list3}",end="\t\t")
print(f"list3 address:{id(list3)}")
print(f"======== set {'list4'}={'list3'} ========")
print(f"list4:{list4}",end="\t\t")
print(f"list4 address:{id(list4)}")
print()

list4.append('D')
print(f"======== add {'D'} to {'list4'} ========")
print(f"list3:{list3}",end="\t")
print(f"list3 address:{id(list3)}")
print(f"list4:{list4}",end="\t")
print(f"list4 address:{id(list4)}")






