#封装

#私有方法在类外不允许被对象调用,但是可以在公有方法内调用(对象名调用公有方法,公有方法内部再调用私有方法)
class Student:
	#属性前加两个__表示私有属性,在类外不能通过'对象名.属性'去访问,类内的方法可以访问私有属性
	def __init__(self,name,score):
		self.name=name
		self.__score=score

	def getScore(self):
		return self.__score

	def setScore(self,score):
		if 0<=score<=100:
			self.__score=score
		else:
			print(f"成绩必须在0到100之间.")
			return None

	#方法前加两个__表示私有方法,在类外不能通过'对象名.方法'去访问,'__showInfo'改为了'_Student__showInfo'
	def __showInfo(self):
		print(f"我是:{self.name},分数是:{self.__score}.")

student=Student('张三',90)
print(f"{student.name}的成绩为:{student.getScore()}")

student.setScore(95)
print(f"{student.name}的成绩为:{student.getScore()}")

student.setScore(-100)
print(f"{student.name}的成绩为:{student.getScore()}")

student._Student__showInfo()

#查看对象属性和类的方法(私有属性和方法都被改名了)
print(student.__dict__)
print(Student.__dict__)
