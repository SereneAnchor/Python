#10.__iter__,__next__:返回迭代器、返回下一个元素
class A:
	def __init__(self,maxNum):
		self.maxNum=maxNum
		self.current=0

	#返回当前对象,在for循环中时自动调用
	def __iter__(self):
		return self

	#返回下一个对象,next(obj)时自动调用
	def __next__(self):
		if self.current<self.maxNum:
			self.current+=1
			return self.current
		raise StopIteration

a1=A(3)
print(next(a1),end=" ")
print(next(a1),end=" ")
try:
	print(next(a1))
except StopIteration:
	print(f"迭代停止...")
print(f"*"*10)
a2=A(5)
for num in a2:
	print(num,end=" ")
print()


#11.__enter__,__exit__:进入上下文、退出上下文释放资源
class B:
	#进入with之前,自动调用
	def __enter__(self):
		print(f"进入 with")
		return "资源对象"

	#离开with后,自动调用
	def __exit__(self, exc_type, exc_val, exc_tb):
		print(f"退出with")
		print(f"异常类型:{exc_type}")
		print(f"异常值:{exc_val}")

with B() as resource:
	print(resource)







