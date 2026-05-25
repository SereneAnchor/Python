#1、运算符:+、-、*、/(返回浮点数)、//(向下取整)、%(取余数)、**(幂运算)
a=10
b=3
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a}//{b}={a//b}")
print(f"{a}**{b}={a**b}")

#2、赋值运算符、比较运算符(返回布尔值)、逻辑运算符(and:都真才真、or:有真就为真、not:取反)返回布尔值

"""
	3、if判断(必须+冒号)
	单分支->if:
	双分支->if:	else:
	多分支->if:	elif:	elif:	elif:
	嵌套分支
"""
#条件表达式结合逻辑运算符
hour=int(input("输入当前小时数(0-23):"))
today=input("输入是否为工作日(是/否):")
if 9<=hour<=18 and today=="是":
	print("未到下班时间请认真工作.")
else:
	print("当前为休息日请好好休息.")

#三元表达式与双分支
age=25
result="成年" if age>=18 else "未成年"

if age>=18:
	result="成年"
else:
	result="未成年"

