""""
装饰器:特殊的闭包函数,不修改原有函数源代码、不改变原有函数调用方式,动态为函数新增额外功能
必备条件:	函数嵌套、内层引用外层函数、外层返回内层函数、在内层函数调用原函数之前、之后进行装饰
"""

#1.基础装饰器(无语法糖)

#原函数
def playGame():
	print(f"王者荣耀,启动!")

#定义装饰器(外层函数outerFunc接收原函数playGame)
def outerFunc(func):
	#定义一个内层函数,该函数使用外层函数的参数,innerFunc在调用原函数之前增加登录校验功能
	def innerFunc():
		#装饰:新增登录校验功能
		print(f"innerFunc 登录校验...")
		#执行原函数的功能
		func()
	return innerFunc

#'='左侧的Func相当于innerFunc函数,把原函数playGame传递给func
Func=outerFunc(playGame)
Func()
print('='*60)

#2.语法糖装饰器

#定义装饰器
def outer(func):
	def inner():
		print(f"inner 登录校验...")
		func()
	return inner

#语法糖:原函数comment使用了@outer,相当于comment=outer(comment),outer返回的inner赋给comment
@outer
def comment():
	print(f"comment 发表评论")
comment()

