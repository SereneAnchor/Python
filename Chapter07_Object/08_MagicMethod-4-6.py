#4.__len__:返回长度
class A:
	def __init__(self,data):
		self.data=data

	#返回列表的长度,len(obj)时自动调用
	def __len__(self):
		return len(self.data)

a=A([1,2,3])
print(f"__len__:{len(a)}")


#5.__getitem__:读取元素
class B:
	def __init__(self):
		self.data={'name':'Tom','age':22}

	#根据key取值,obj[key]时自动调用
	def __getitem__(self,key):
		#data是一个字典,默认判断key是否在字典的键里面
		if key not in self.data:
			return None
		return self.data[key]

b=B()
print(f"__getitem__:{b['name'],b['age']}")


#6.__setitem__:设置元素
class C:
	def __init__(self):
		self.data={}

	def __str__(self):
		return f"{self.data}"

	#设置对象字典的键值对,obj[key]=value时自动调用
	def __setitem__(self,key,value):
		self.data[key]=value

c=C()
c['name']='Tom'
c['age']=24
print(c)
