#魔法方法:方法前后都有双下划线(类的私有方法是前面有双下划线),这些方法是Python在某些场景下自动调用的

#1.__new__方法,创建对象的过程包括先创建对象再初始化对象
class Person:
	#__new__方法必须返回对象实例,返回None时__init__不会正常执行,cls代表类名(Person)
	def __new__(cls,name):
		print(f"__new__:创建对象")
		object=super().__new__(cls)
		return object

	def __init__(self,name):
		print(f"__init__:初始化对象")
		self.name=name

person=Person('Tom')

#2.__str__方法,用来定义对象给"用户"看的字符串
class Animal:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	#打印对象名不再是输出对象地址,而是输出该方法返回的字符串
	def __str__(self):
		return f"{self.name},{self.age}岁"

animal=Animal('人',18)
print(animal)