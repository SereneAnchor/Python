#魔法方法:方法前后都有双下划线(类的私有方法是前面有双下划线),这些方法是Python在某些场景下自动调用的

#1.__new__方法:创建对象
class A:
	#__new__方法必须返回对象实例,返回None时__init__不会正常执行,cls代表类名(Person)
	def __new__(cls,name):
		print(f"__new__:__new__创建对象",end="\t")
		object=super().__new__(cls)
		return object

	def __init__(self,name):
		print(f"__init__初始化对象")
		self.name=name

a=A('Tom')

#2.__str__方法:返回面向用户的字符串
class B:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	#打印对象名不再是输出对象地址,而是输出该方法返回的字符串,str(obj)或者print(obj)时自动调用
	def __str__(self):
		return f"{self.name},{self.age}岁"

b=B('祖国人',18)
print(f"__str__:{str(b)}")
#默认调用__str__
#print(b)

#3.__repr__:返回面向开发者的字符串
class C:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	#repr(obj)时自动调用,无__str__方法时作为备用
	def __repr__(self):
		return f"name={self.name!r},age={self.age!r}"

c=C('Bob',20)
print(f"__repr__:{repr(c)}")

"""
__str__和__repr__都能在打印对象时输出指定的字符串
如果实现了__str__方法就优先调用__str__;否则没有实现__str__的话再去查找__repr__
"""




