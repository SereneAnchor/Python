import functools

#1.多个装饰器装饰同一个函数:从上到下装饰包裹,从下到上执行逻辑
def checkLogin(func):
	def inner():
		print(f"检测用户是否登录验证.")
		func()
	return inner

def checkPermission(func):
	def inner():
		print(f"检测用户是否具备权限.")
		func()
	return inner

#两个装饰器装饰一个原函数:checkPermission、checkLogin先后装饰原函数
@checkLogin
@checkPermission
def submit():
	print(f"提交申请.")
submit()
print('='*60)

#2.带参数的装饰器,三层函数结构:外层接收自定义参数、中层接收原函数、内层执行业务逻辑
def audit(actionType):
	#中层接收原函数
	def decorator(func):
		#内层执行业务逻辑
		def inner(user,amount):
			if actionType=='recharge':
				print(f"--[审计]--用户在进行充值操作.")
			elif actionType=='withdraw':
				print(f"--[审计]--用户在进行提现操作.")
			elif actionType=='transfer':
				print(f"--[审计]--用户在进行转账操作.")
			result=func(user,amount)
			return result
		return inner
	return decorator

#audit('recharge')会返回decorator,等价于使用中层函数来修饰wallet,外层的主要作用是让内层捕获recharge
@audit('recharge')
def wallet(user,amount):
	print(f"\"{user}\"账户变动金额:{amount}")
	return f"操作成功:{amount}"
print(wallet('SereneAnchor',250))
print('='*60)

#3.装饰器保留原函数的信息,原函数指向了inner,所以原函数的名称、文档等信息可能丢失
def timer(func):
	#把原函数的重要信息复制给包装函数inner
	@functools.wraps(func)
	def inner(*args,**kwargs):
		return func(*args,**kwargs)
	return inner

@timer
def calculate():
	"""
	 *  @brief  完成数值计算
	 *  @param  None
	 *  @return None
	 *  @author SereneAnchor
	 *  @date   2026-07-14
	"""
	pass

#打印原函数名字:没有timer装饰器时能够正确打印
print(f"{calculate.__name__}")
print(f"{calculate.__doc__}")

