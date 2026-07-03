"""
作用域分为全局作用域(函数外部)、局部作用域(函数内部)
变量分为全局变量(定义在函数外部)、局部变量(定义在函数内部)
"""
numA=20
def getNumA():
	numB=50
	print(f"函数内numA:{numA}")
	print(f"函数内numB:{numB}")
getNumA()
print(f"函数外numA:{numA}")

#global关键字的用法(修改不可变类型的变量要使用global,可变类型可以不加global)
"""
	1、可变类型:list、dict、set、自定义类型(类),尽管数据相同但是占用不同的内存空间(不同变量指向不同内存)
	2、不可变类型:int、bool、str、double、tuple,相同的数据在内存中只存储1份(不同变量指向同一内存)
	a=10	b=10	那么a和b存储的都是10的地址
"""

#可变类型
person={'name':'彭兵幸','age':250}
print(f"person全局地址:{id(person)}")
def getPerson1():
	person={'name':'彭兵幸','age':250}
	print(f"函数1内全局地址:{id(person)}")
getPerson1()

def getPerson2():
	person['sex']='male'
	print(f"函数2内全局地址:{id(person)}")
getPerson2()

#不可变类型
numC=30
def getNumB():
	global numC
	numC=300
getNumB()
print(f"函数外numC:{numC}")