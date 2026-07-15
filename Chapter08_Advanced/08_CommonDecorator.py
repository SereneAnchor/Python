import time
import functools

"""
1.自定义函数装饰器时,通常要写:@functools.wraps(func),它不会改变原函数的业务执行结果,只会给包装函数复制原函数的名称、文档
等元数据,保留这些信息更规范
2.包装函数应该尽可能保持原函数的调用约定:只增加计划中的额外功能,不应意外破坏原函数的参数、返回值和函数信息
"""

#1.耗时统计装饰器
def costTime(func):
	@functools.wraps(func)
	def inner(*args,**kwargs):
		start=time.time()
		result=func(*args,**kwargs)
		end=time.time()
		print(f"函数\"{func.__name__}\"执行耗时:{end-start:.4f}秒.")
		#包装函数要尽可能保持和原函数一样的参数、返回值、调用效果
		return result
	return inner

@costTime
def heavyTask():
	sum=0
	for i in range(100000):
		sum+=i
	#原函数的返回值会保存在inner包装函数内
	return sum
heavyTask()
print('='*60)

#2.异常捕获装饰器,给多个原函数统一加上一层try-catch,避免每个原函数内部都重复编写异常捕获代码
def catchError(func):
	@functools.wraps(func)
	def inner(*args,**kwargs):
		try:
			return func(*args,**kwargs)
		except Exception as error:
			print(f"函数执行异常:{error}")
			return None
	return inner

@catchError
def divide(a,b):
	return a/b
print(divide(3,0))
print('='*60)

#3.类装饰器拓展,依靠__call__魔法方法让类实例可以被调用
class LogDecorator:
	def __init__(self,func):
		self.func=func
		functools.update_wrapper(self,func)

	def __call__(self, *args, **kwargs):
		print(f"类装饰器:函数开始执行...")
		result=self.func(*args,**kwargs)
		print(f"类装饰器:函数执行完成...")
		return result

@LogDecorator
def test():
	print(f"执行业务逻辑")
test()
print('='*60)


#4.带参数的通用日志装饰器
def logAction(actionType):
	#中层接收被装饰函数
	def decorator(func):
		@functools.wraps(func)
		#内层执行逻辑处理
		def inner(*args,**kwargs):
			print(f"正在执行【{actionType}】数据操作.")
			#执行原函数并保留返回值
			result=func(*args,**kwargs)
			#返还原函数结果
			return result
		return inner
	return decorator

#测试1
@logAction('查询')
def queryData(tableName):
	print(f"正在读取数据表:{tableName}")
	return "数据读取完成."

#测试2
@logAction('录入')
def insertData(tableName,count):
	print(f"向{tableName}插入{count}条记录")
	return "数据录入完成."

#测试3
@logAction('移除')
def removeData(rowId):
	print(f"删除行号:{rowId}的数据")
	return "删除数据完成."

if __name__=='__main__':
	print(queryData('salesData'))
	print('*'*25)
	print(insertData('userInfo',30))
	print('*'*25)
	print(removeData(250))
