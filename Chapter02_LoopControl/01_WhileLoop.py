#While循环

#求1...50的和
i=1
sum=0
while i<=50:
	sum+=i
	i+=1
print(f"sum is:{sum}")

#求1...50之间所有奇数的和
i=1
sum=0
while i<=50:
	if i%2!=0:
		sum+=i
	i+=1
print(f"sum is:{sum}")

#break用法
i=1
while i<=50:
	if i%15==0:
		break
	print(i,end=" ")
	i+=1
print("break程序结束.")

#continue用法
i=1
while i<=50:
	if i%6==0:
		#i必须先自增,遇到continue时直接转到while条件判断处
		i+=1
		continue
	print(i,end=" ")
	i+=1
print("continue程序结束.")

#猜数字
num=15
count=1
print("=====猜数字游戏(1->30之间,3次机会)=====")
while True:
	answer=int(input(f"输入数字(剩余{3-count+1}次机会):"))
	if answer==num:
		print("猜对了.")
	elif answer>num:
		print("猜大了.")
	else:
		print("猜小了.")
	if count>=3:
		print(f"次数用完.正确答案是:{num}")
		break
	count+=1
