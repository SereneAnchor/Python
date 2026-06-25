#方法重写:子类中重写父类的方法

class Animal:
	def __init__(self,name):
		self.name=name

	def showInfo(self):
		print(f"{self.name} showInfo.")

	def speak(self):
		print(f"{self.name} speak.")

class Dog(Animal):
	def __init__(self,name,age):
		self.name=name
		self.age=age

	#子类重写父类的成员方法,子类对象调用子类的同名方法
	def showInfo(self):
		print(f"{self.name} showInfo.")

	def speak(self):
		print(f"{self.name} speak.")

#子类对象调用本类还是父类的方法,取决于mro的查找顺序
dog=Dog('旺财',2.5)
dog.showInfo()
dog.speak()
print(Dog.__mro__)

#子类调用父类方法:super().父类方法名(参数1,参数2...);	父类名.方法名(self,参数1,参数2...)
class Cat(Animal):
	def __init__(self,name,age):
		#子类中通过super调用父类方法
		super().__init__(name)
		self.age=age

	def showInfo(self):
		super().showInfo()
		print(f"{self.name} showInfo.")

cat=Cat('橘猫',2.5)
cat.showInfo()
