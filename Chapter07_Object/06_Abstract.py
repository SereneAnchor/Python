#抽象方法:方法中没有具体实现,只写pass

#抽象类:类中只有抽象方法

class NoteBook:
	def show(self):
		pass

	def cpuCompute(self):
		pass

	def gpuCompute(self):
		pass

	def fanHeat(self):
		pass

#子类继承抽象类
class ASUS(NoteBook):
	def show(self):
		print(f"华硕 show.")

	def cpuCompute(self):
		print(f"华硕 CPU.")

	def gpuCompute(self):
		print(f"华硕 GPU.")

	def fanHeat(self):
		print(f"华硕 散热.")

class MyNoteBook(NoteBook):
	def show(self):
		print(f"我的 show.")

def test(notebook:NoteBook):
	notebook.show()
	notebook.cpuCompute()
	notebook.gpuCompute()
	notebook.fanHeat()

if __name__=='__main__':
	asus=ASUS()
	test(asus)
	print(f"*"*20)
	myNoteBook=MyNoteBook()
	test(myNoteBook)


