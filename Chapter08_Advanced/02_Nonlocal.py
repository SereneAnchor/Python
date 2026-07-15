"""
变量赋值二义性:Python中'='存在二义性,左侧变量会优先被判定为本地局部变量,如果闭包内层函数直接修改外层变量,
会因为找不到本地变量报错,此时需要'nonlocal'声明外层变量

闭包会持续捕获、引用外部函数的变量,导致外层函数的变量无法被垃圾回收,长期占用内存,大量使用闭包可能造成内存资源消耗
"""
def outerFunc():
	num=10
	#这里只是定义内部函数,并没有开始调用
	def innerFunc():
		#赋值优先被当作定义,因此并不会修改外层函数的num;当前的num是属于内部函数的局部变量
		num=20
		print(f"innerFunc num:{num}")
	innerFunc()
	print(f"outerFunc num:{num}")
	return innerFunc

outerFunc()

#nonlocal示例1
def func1():
	num1=100
	def func2():
		#使用nonlocal表示num1不是本地变量,通知解释器去外层查找num1
		nonlocal num1
		num1=200
		print(f"func2 num1:{num1}")
	func2()
	print(f"func1 num1:{num1}")
	return func2
func1()

#nonlocal示例2
def func3():
	num2=10
	def func4():
		nonlocal num2
		num2=num2+20
		print(f"func4 num2:{num2}")
	func4()
	print(f"func3 num2:{num2}")
	return func4
func3()

#外层变量是可变对象如列表、字典等,仅修改容器内部元素、不对变量整体重新赋值时,无需使用nonlocal关键字
def func5():
	data=[1,2,3]
	def func6():
		#仅修改列表内部元素,无整体赋值
		data.append(4)
		data.extend([5,6])
		print(f"func6 data:{data}")
	func6()
	print(f"func5 data:{data}")
	return func6
func5()
