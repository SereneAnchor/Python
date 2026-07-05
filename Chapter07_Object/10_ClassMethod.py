#类方法使用'@classmethod'装饰器,第一个参数通常是cls表示当前类,不直接访问实例属性,通常访问类属性
class Student:
	#类属性
	count=0

	def __init__(self,name):
		self.name=name
		Student.count+=1

	#类方法,可以通过对象和类名来调用,cls等价于Student
	@classmethod
	def showCount(cls):
		print(f"学生人数:{cls.count}")

student1=Student('张三')
student2=Student('李四')
student1.showCount()
Student.showCount()