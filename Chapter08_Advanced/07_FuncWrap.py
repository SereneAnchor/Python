#自定义一个带参数的装饰器,模仿functools.wraps函数

#func1=calculate
def funcWrap(func1):
	def decorator(func2):
		def inner(*args,**kwargs):
			return func2(*args,**kwargs)
		inner.__name__=func1.__name__
		inner.__doc__=func1.__doc__
		return inner
	return decorator

def timer(func):
	@funcWrap(func)
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

#打印函数名字
print(f"{calculate.__name__}")
print(f"{calculate.__doc__}")

