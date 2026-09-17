#1.捕获特定异常
def safeDivide(a,b):
	try:
		result=a/b
	except ZeroDivisionError:
		print(f"错误:除数不能为0")
		return None
	return result

print(safeDivide(10,2))
print(safeDivide(10,0))

#2.文件操作中的异常处理
def safeReadFile(fileName):
	try:
		with open(fileName,'r',encoding='utf-8') as file:
			content=file.read()
		return content
	except FileNotFoundError:
		print(f"错误:文件'{fileName}'不存在")
		return None
safeReadFile('AAA.ttx')

#3.多个except块
try:
	with open('AAA.txt','r',encoding='utf-8') as file:
		content=file.read()
except FileNotFoundError:
	print(f"错误:文件不存在")
except PermissionError:
	print(f"错误:没有权限")
except UnicodeDecodeError:
	print(f"错误:编码错误")

#4.一个except捕获多个异常
try:
	with open('AAA.txt','r',encoding='utf-8') as file:
		content=file.read()
except (FileNotFoundError,PermissionError):
	print(f"错误:文件访问失败")

#5.获取异常信息
try:
	with open('AAA.txt','r',encoding='utf-8') as file:
		content=file.read()
except FileNotFoundError as error:
	print(f"异常类型:{type(error)}")
	print(f"异常信息:{error}")

#6.完整异常处理(try成功、else、finally;try失败、except、finally)
try:
	with open('AAA.txt','r',encoding='utf-8') as file:
		content=file.read()
except FileNotFoundError:
	print(f"错误:文件不存在")
except Exception as error:
	print(f"发生错误:{error}")
else:
	#只有try语句块成功执行、不报异常时才执行
	print(f"读取成功,内容长度:{len(content)}字符")
finally:
	#finally语句块必被执行
	print(f"文件操作完成")

#7.finally语句块的用途(不推荐这样打开文件,应该使用with方式)
file=None
try:
	file=open('AAA.txt','r',encoding='utf-8')
	content=file.read()
except FileNotFoundError:
	print(f"错误:文件不存在")
finally:
	#只有file打开了才需要关闭
	if file is not None:
		file.close()
		print(f"文件已关闭")

#8.异常传播
def Func1():
	Func2()

def Func2():
	x=1/0

def main():
	try:
		Func1()
	except ZeroDivisionError:
		print(f"捕获到异常:除以0")

main()