"""
变量作用域
	全局作用域:整个py文件;全局作用域无法访问局部变量
	局部作用域:某个函数或者类内;局部作用域中默认读取全家变量,如果要修改全局变量,需要使用global关键字
LEGB作用域
	L:局部作用域,如函数内
	E:嵌套作用域,多个函数嵌套,内层函数要访问的变量在外层函数中定义,也就是闭包技术
	G:全局作用域,py文件内定义
	B:内置定义域,如print,len内
global:在函数内部修改全局变量,无法操作嵌套的函数变量
nonlocal:闭包内部修改外层函数变量,无法操作全局变量
"""


"""
闭包:在函数嵌套的前提下,内部函数使用了外部函数的变量,并且外部函数返回了内部函数,这个引用外层变量的内部函数就是闭包
	有嵌套:外层函数内层函数的嵌套结构
	有引用:内层函数使用外层函数的局部变量、参数等
	有返回:外层函数将内层函数作为返回值返回
"""
def fun1(num1):

	def fun2(num2):
		num=num1+num2
		print(f"num:{num}")
	return fun2
f2=fun1(3)
f2(5)

"""
变量赋值二义性:Python中'='存在二义性,左侧变量会优先被判定为本地局部变量,如果闭包内层函数直接修改外层变量,会因为找不到
	本地变量报错,此时需要'nonlocal'声明外层变量
"""
def fun3():
	num3=10
	def fun4():
		#赋值优先被当作定义
		num3=20
		print(f"fun4 num3:{num3}")
	fun4()
	print(f"fun3 num3:{num3}")
	return fun4

#fun3()

#nonlocal示例1
def fun5():
	num5=100
	def fun6():
		#使用nonlocal表示不是本地变量,通知解释器去外层查找num5
		nonlocal num5
		num5=200
		print(f"fun6 num5:{num5}")
	fun6()
	print(f"fun5 num5:{num5}")
	return fun6
fun5()

#nonlocal示例2
def fun7():
	num7=10
	def fun8():
		nonlocal num7
		num7=num7+20
		print(f"fun8 num7:{num7}")
	fun8()
	print(f"fun7 num7:{num7}")
	return fun8
fun7()

#外层变量是可变对象如列表、字典等,仅修改容器内部元素、不对变量整体重新赋值时,无需使用nonlocal关键字
def fun9():
	data=[1,2,3]
	def fun10():
		#仅修改列表内部元素,无整体赋值
		data.append(4)
		data.extend([5,6])
		print(f"fun10 data:{data}")
	fun10()
	print(f"fun9  data:{data}")
	return fun9
fun9()

#自由变量


