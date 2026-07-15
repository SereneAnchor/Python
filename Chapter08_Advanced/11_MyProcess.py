#自定义Process类,继承Process,重写run方法

import multiprocessing
import time

class MyProcess(multiprocessing.Process):
	def __init__(self,name,delayTime):
		#初始化从父类中继承过来的某些属性,如pid
		super().__init__()
		self.name=name
		self.delayTime=delayTime

	#重写run方法,进程启动后(也就是start)会自动执行
	def run(self):
		print(f"自定义进程:{self.name}启动,PID:{self.pid}")
		time.sleep(self.delayTime)
		print(f"自定义进程:{self.name}结束.")

if __name__=='__main__':
	p=MyProcess('X',2)
	p.start()
	p.join()
	print(f"主进程结束.")