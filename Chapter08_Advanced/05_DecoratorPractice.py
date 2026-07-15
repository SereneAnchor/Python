#装饰器实战:原函数和返回的inner函数绑定

#1.装饰有参数无返回值函数
def outer1(func):
	def inner1(a,b):
		print(f"inner1 开始计算...")
		func(a,b)
	return inner1
@outer1
def getSum1(x,y):
	z=x+y
	print(f"两数之和为:{z}")
print(f"outer1:{getSum1(1,2)}")
print('='*60)

#2.装饰无参数有返回值函数
def outer2(func):
	def inner2():
		print(f"inner2 开始计算...")
		result=func()
		print(f"inner2 计算成功...")
		return result
	return inner2
@outer2
def getSum2():
	return 10+15
print(f"outer2:{getSum2()}")
print('='*60)

#3.装饰有参数有返回值函数
def outer3(func):
	#内层函数的参数要与原函数保持一致
	def inner3(a,b):
		print(f"inner3 开始计算...")
		result=func(a,b)
		print(f"inner3 计算成功...")
		return result
	return inner3
@outer3
def getSum3(x,y):
	z=x+y
	return z
print(f"outer3:{getSum3(1,2)}")
print('='*60)

#4.装饰可变位置参数
def outer4(func):
	#内层函数接收可变位置参数,args本质上是一个元组,func(*args)就是将元组中的数据拆包,拆成一个一个的位置参数
	def inner4(*args):
		print(f"args={args}")
		result=func(*args)
		print(f"inner4 计算成功...")
		return result
	return inner4
@outer4
def getSum4(a,b,c):
	return a+b+c
print(f"outer4:{getSum4(3,5,8)}")
print('='*60)

#5.装饰可变关键字参数
def outer5(func):
	#内层函数接收可变关键字参数,kwargs本质上是一个字典,func(**kwargs)将字典中的数据拆包成key=value的形式
	def inner5(**kwargs):
		print(f"kwargs={kwargs}")
		result=func(**kwargs)
		print(f"inner5 计算成功...")
		return result
	return inner5
@outer5
def getSum5(a,b):
	return a+b
print(f"outer5:{getSum5(a=1,b=2)}")
print('='*60)

#6.装饰可变参数(*args、**kwargs)
def outer6(func):
	def inner6(*args,**kwargs):
		print(f"inner6 开始计算...")
		#将元组、字典拆包传递给原函数
		result=func(*args,**kwargs)
		print(f"inner6 计算成功...")
		return result
	return inner6
@outer6
def getSum6(*args,**kwargs):
	print(f"args:{args}\tkwargs:{kwargs}")
	sum=0
	#累加位置参数
	for i in args:
		sum+=i
	#累加关键字参数
	for i in kwargs.values():
		sum+=i
	return sum
print(f"outer4:{getSum6(1,2,3,a=100,b=200,c=300)}")
print(f"getSum4.name:{getSum6.__name__}")
print('='*60)




