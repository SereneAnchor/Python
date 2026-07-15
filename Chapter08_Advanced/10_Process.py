#Windows系统中,必须把进程启动代码放入if __name__=='__main__'中,否则无限递归创建进程

#使用Process手动创建子进程
import multiprocessing
import time

def task(name,delayTime):
	"""
	 *  @brief  进程执行需要执行任务,自定义一个任务
	 *  @param  name		接收子进程的名字
	 *  @parm	delayTime	接收子进程延迟的时间
	 *  @author SereneAnchor
	 *  @date   2026-07-13
	"""
	print(f"子进程:{name}启动,PID:{multiprocessing.current_process().pid}")
	time.sleep(delayTime)
	print(f"子进程:{name}结束.")

print(f"main外进程PID:{multiprocessing.current_process().pid}\t__name__:{__name__}")

#只有主进程能进入判断
if __name__=='__main__':
	print(f"主进程PID:{multiprocessing.current_process().pid}")
	#创建两个子进程,参数传递可以是元组和字典
	p1=multiprocessing.Process(target=task,args=('p1',2))
	p2=multiprocessing.Process(target=task,kwargs={'name':'p2','delayTime':3})
	#启动子进程,子进程执行顺序随机(子进程会从当前文件上往下全部执行一遍)
	p1.start()
	p2.start()
	#显示等待子进程执行完毕
	p1.join()
	p2.join()
	print(f"主进程退出.")
	

