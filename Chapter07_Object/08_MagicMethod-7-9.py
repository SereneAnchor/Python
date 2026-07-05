#7.__del__:删除元素
class A:
	def __init__(self):
		self.data={'name':'Tom','age':26}

	#del obj[key]时自动调用
	def __delitem__(self,key):
		del self.data[key]

a=A()
print(a.data)
del a['name']
print(a.data)

#8.__contains__:判断是否包含
class B:
	def __init__(self):
		self.data={'name':'Tom','age':28}

	#key in obj时自动调用
	def __contains__(self,key):
		return key in self.data

b=B()
print('name' in b)
print('sex' in b)

#9.__call__:对象像函数一样调用
class C:
	#obj(a,b)时自动调用
	def __call__(self,x,y):
		return x+y

c=C()
print(c(1,2))