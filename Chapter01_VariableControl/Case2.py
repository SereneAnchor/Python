#1、输入一个整数,判断其是奇数还是偶数
num=int(input("输入一个整数:"))
flag=True if num%2==0 else False
if flag:
	print(f"{num}是偶数.")
else:
	print("{}是奇数.".format(num))


#2、输入一个人的身高(m)和体重(kg),计算BMI指数(体重/身高平方)
height=float(input("输入身高:"))
weight=float(input("输入体重:"))
BMI=weight/(height**2)
print(f"BMI:{BMI:.2f}")


#3、模拟超市会员打折,非会员无折扣,会员消费满200减50,不满200打九折,输入会员状态和消费金额,格式化输出消费金额
flag=input("会员状态(是/否):")
cost=float(input("消费金额:"))

if flag=="是":
	if cost<200:
		print("会员消费金额:{:.2f} 实际消费:{:.2f}".format(cost,cost*0.9))
	else:
		print("会员消费金额:{:.2f} 实际消费:{:.2f}".format(cost,cost-50))
else:
	print("非会员应当支付:{:.2f}".format(cost))
