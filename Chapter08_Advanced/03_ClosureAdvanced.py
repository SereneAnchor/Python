#1.自由变量:就是被内层函数引用的外层函数变量,闭包会把这些变量保存在函数内置属性中,阻止垃圾回收
def outerFunc():
	num=10
	age=20
	def innerFunc():
		print(f"innerFunc num:{num}")
		print(f"innerFunc age:{age}")
	return innerFunc
func=outerFunc()
#查看自由变量名称、闭包保存的变量对象
print(f"自由变量:{func.__code__.co_freevars}")
#print(f"闭包保存的变量对象:{func.__closure__}")

#2.闭包陷阱,循环延迟绑定:循环批量生成闭包时,所有闭包会共用同一个外层变量,最终取值均为循环最后值

#错误案例:inner定义时没有保存i的值,而是真正调用时才去查找i,所以全部输出2,而非0、1、2;for循环中的i是全局变量
funcs=[]
for i in range(3):
	#内部函数使用了i,触发闭包机制,将i打包成cell,放入inner.__closure__,内部函数访问i是获取i内存中的数据
	def inner():
		print(i,end="\t")
	#将函数存储到列表中
	funcs.append(inner)
funcs[0]()
funcs[1]()
funcs[2]()
print()

#正确案例:参数立即绑定值
funcs=[]
for i in range(3):
	#内部函数没有使用外部循环变量i,而是赋给了内层函数变量x,给参数x设置默认值为i,不会触发闭包机制
	def inner(x=i):
		print(x,end="\t")
	funcs.append(inner)
funcs[0]()
funcs[1]()
funcs[2]()
print()

#3.闭包内存释放,闭包会造成内存常驻,无需使用时可手动解除引用,释放内存:func=None
def outer():
	name='张三'
	age=23
	def inner():
		print(f"inner name:{name}")
		print(f"inner age:{age}")
	return inner
func=outer()
func()
print(func.__code__.co_freevars)
print(func.__closure__)

#将闭包函数设置为None,回收func,自动回收cell
func=None

#4.闭包案例:累加案例,持续保留上一次的计算结果
def func1():
	result=0
	#num用来接收外部传递的实参
	def func2(num):
		#将外层函数的result声明为nonlocal,达到修改外层函数变量的效果
		nonlocal result
		result+=num
		return result
	return func2
#Func等价于func2
Func=func1()
#num为1,result为0+1=1,func2返回1;num为2,result为1+2=3,func2返回3;num为3,result为3+3=6,func2返回6
print(f"闭包案例:{Func(1)}\t{Func(2)}\t{Func(3)}")
