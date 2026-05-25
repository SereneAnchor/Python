#推导式:由一个数据序列构建另一个新的数据序列的结构体

#列表推导式:创建一个0到9的列表,常见写法是使用while、for循环;
"""
	取出列表中的每一个变量执行表达式后得到的结果放到新列表中
	变量名=[表达式 for 变量 in 列表]
	变量名=[表达式 for 变量 in 列表 if 条件]
	变量名=[表达式 for 变量 in 列表 for 变量 in 列表]
"""

#生成0-9的列表
list1=[ele for ele in range(10)]
print(f"list1:{list1}")

#生成偶数列表
list2=[ele for ele in range(10) if ele%2==0]
print(f"list2:{list2}")

#生成矩阵列表
list3=[(row,col) for row in range(3) for col in range(4)]
print(f"list3:{list3}")


#使用列表推导式生成平方数集合(输入10就生成1-10中每一个数字的平方)
number=int(input("enter a number:"))
list1=[ num**2 for num in range(1,number+1)]
print(f"list1:{list1}")
