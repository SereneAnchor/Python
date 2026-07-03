#类基础

#定义简单类:pass表示暂时不写内容
class Student:
	#类属性:可以通过对象名和类名来访问
	school='江西省于都县第二中学'
	count=0

	"""
		构造方法:创建对象是自动执行,self代表当前创建的对象,构造方法自动返回创建的对象
		name、age属于实例属性,创建对象时每个对象的实例属性不同
	"""
	def __init__(self,name,age):
		self.name=name
		self.age=age
		#每创建一个对象计数+1,计数为类属性
		Student.count+=1

	#成员方法,第一个参数通常也是self(成员方法是否都必须要self参数)
	def showInfo(self):
		print(f"我叫:{self.name},今年:{self.age}岁.")

#pass


#创建类的对象:对象名存储对象在内存中的地址(变量存储在栈区,对象存储在堆区)
student1=Student('SerenaAnchor',20)

#student会自动传递给showInfo的self
student1.showInfo()


print(student1.school)
print(Student.school)
print('*'*20)

#通过类名修改类属性值
Student.school='江西财经大学'
print(student1.school)
print(Student.school)
print('*'*20)

#通过对象名修改则是给该对象添加对象属性,赋值具有二义性
student1.school='江西财经大学现代经济管理学院'
print(student1.school)
print(Student.school)

print(student1)
#print(Student.__dict__)
