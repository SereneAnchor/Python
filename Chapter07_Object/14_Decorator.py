""""
装饰器:特殊的闭包函数,不修改原有函数源代码、不改变原有函数调用方式,动态为函数新增额外功能
必备条件:	函数嵌套、内层引用外层函数、外层返回内层函数、调用原函数之前进行装饰
"""

#1.基础装饰器(无语法糖)

#原函数
def playGame():
	print(f"王者荣耀,启动!")

#定义装饰器(外层函数outerFun接收原函数playGame)
def outerFun(func):
	#定义一个内层函数,该函数使用外层函数的参数,装饰器就是内层函数使用外层函数的形参(func函数,也就是原函数)
	def innerFun():
		#新增登录校验功能
		print(f"登录校验...")
		#执行原函数的功能
		func()
	return innerFun

#'='左侧的playGame相当于innerFun函数
playGame=outerFun(playGame)
playGame()



