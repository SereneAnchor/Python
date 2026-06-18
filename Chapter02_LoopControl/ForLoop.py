#for循环,in后接的是一个可迭代对象如:list、tuple、dict、set等

#range(start,stop,step):返回一个左闭右开的可迭代对象,range(4)等价于range(0,4)等价于range(0,4,1)

#求1...50的奇数和
sum=0
for i in range(51):
	if i%2!=0:
		sum+=i
print(f"sum is:{sum}")

#用户登录:username->SereneAnchor 密码825210647
for i in range(2):
	username=input("输入用户名:")
	password=input("输入密码:")
	if username=="SereneAnchor":
		if int(password)==825210647:
			print("登陆成功.")
			break
		else:
			print(f"密码错误,剩余:{1-i}次机会.")
	else:
		print(f"用户名错误,剩余:{1-i}次机会.")

#for循环中break的else结构,else代码不执行
str="python"
for i in str:
	if i=='h':
		print("遇到\'h\'不打印.")
		break
	print(i,end=" ")
else:
	print("break-for循环正常结束.")

#for循环中continue的else结构,else代码会执行
str="python"
for i in str:
	if i=='h':
		print("遇到\'h\'不打印.",end=" ")
		continue
	print(i,end=" ")
else:
	print("continue-for循环正常结束.")

#打印9*9乘法表
for row in range(1,10):
	for colum in range(1,row+1):
		print(f"{row}*{colum}={row*colum}",end="\t")
	print()
