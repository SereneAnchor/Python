#继承

#Teacher、Student类内无任何实现,但继承了Person的Eat、Sleep方法;Person默认继承Object类
class Person:
	def Eat(self):
		print(f"吃东西.")

	def Sleep(self):
		print(f"睡觉.")

class Teacher(Person):
	pass

class Student(Person):
	pass

#teacher对象先在Teacher中查找是否有对应方法,没有的话在Person中查找,没有的话在Object中查找,再无的话直接报错
teacher=Teacher()
teacher.Eat()
teacher.Sleep()

#继承关系中通过子类类名查看对象调用方法的查找顺序
print(Teacher.__mro__)

print('*'*100)

class Animal:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	#Animal的私有方法:在子类中私有方法被改名了,通过Animal.__dict__查看,该方法返回None
	def __Roar(self):
		print(f"Animal Roar.")

class Cat(Animal):
	pass

class Dog(Animal):
	#Dog的构造方法会覆盖掉Animal的同名构造方法,创建对象时只调用Dog的构造方法而不会调用Animal的构造方法
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.type='Dog'

class Bird(Animal):
	#Bird继承Animal,共性的属性可以在Animal的构造方法中初始化,独有的属性在Bird的构造方法中初始化
	def __init__(self,name,age,type):
		#调用Animal的构造方法
		super().__init__(name,age)

		#Bird独有的属性
		self.type=type

#调用的是Animal的构造方法,构造方法中的self永远是外面的对象即cat(cat传递给self、'狸花猫'传递给name、2传递给age)
cat=Cat('狸花猫',2)

dog=Dog('田园犬',1)
print(dog.type)

bird=Bird('知更鸟',5,'Bird')
print(bird.name,bird.age,bird.type)
#print(Bird.__mro__)

#Bird调用Animal的私有方法,Bird.__dict__看不到Animal的私有方法,_Animal__Roar被Bird继承了
bird._Animal__Roar()
dog._Animal__Roar()


#多继承:C同时继承A、B
class BaseA:
	def showInfo(self):
		print(f"BaseA showInfo.")

class BaseB:
	def showInfo(self):
		print(f"BaseB showInfo.")

class C(BaseA,BaseB):
	pass

#先继承哪个类,就先调用哪个类的方法
c=C()
c.showInfo()
print(C.__mro__)