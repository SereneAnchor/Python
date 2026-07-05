"""
	最常见的方法是实例方法,第一个参数是self,实例方法既可以访问实例属性也可以访问类属性
	静态方法使用'@staticmethod'装饰器,不需要访问对象和类,不能通过对象调用静态方法,只能通过类名访问,不访问属性
"""
class MathPool:
	#静态方法,不需要访问对象属性和类属性
	@staticmethod
	def add(a,b):
		return a+b

print(f"add:{MathPool.add(3,5)}")






