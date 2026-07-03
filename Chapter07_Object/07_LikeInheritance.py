#like继承

class Bird:
	def fly(self):
		print(f"Bird fly.")

#is继承,鹰一定是鸟
class Eagle(Bird):
	def fly(self):
		print(f"Eagle fly.")

#like继承,飞机也会飞但不是鸟的派生
class Plane:
	def fly(self):
		print(f"Plane fly.")

def test(bird:Bird):
	bird.fly()

if __name__=='__main__':
	eagle=Eagle()
	test(eagle)
	print("*"*20)
	plane=Plane()
	test(plane)

