#单例模式:无论一个类创建多少对象,都是同一个对象
class Singleton:
	instance=None
	def __new__(cls):
		if cls.instance is None:
			print(f"创建新实例.")
			cls.instance=super().__new__(cls)
		return cls.instance

a=Singleton()
b=Singleton()
print(f"a的地址:{id(a)}")
print(f"b的地址:{id(b)}")
print(a is b)