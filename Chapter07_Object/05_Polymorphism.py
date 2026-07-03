#多态:父类对象引用子类对象,通过父类对象调用方法,能够触发子类对象的方法

class Animal:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def speak(self):
		print(f"{self.name} speak.")

class Dog(Animal):
	def speak(self):
		print(f"{self.name} speak.")

class Cat(Animal):
	def speak(self):
		print(f"{self.name} speak.")

class Duck(Animal):
	def speak(self):
		print(f"{self.name} speak.")

#以不同的子类对象初始化父类对象
def test(animal:Animal):
	animal.speak()

if __name__=='__main__':
	test(Animal('动物',2))
	test(Dog('小狗',3))
	test(Cat('小猫',4))
	test(Duck('鸭子',5))



