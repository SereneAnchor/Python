#lambda表达式为匿名函数

#1.普通函数
def getStr(str):
	return 'Hello '+str

print(f"getStr:{getStr('Python')}")

func1=lambda str:'Hello '+str
print(f"func1:{func1('C++')}")

#2.带参数的lambda表达式(':'之前的为形参,之后的为函数执行逻辑)
func2=lambda num1,num2:num1+num2
print(f"func2:{func2(2,3)}")

#3.带默认参数的lambda表达式(默认参数必须在右侧)
func3=lambda num1,num2=20:num1+num2
print(f"func3:{func3(10)}")

#4.带if/三目运算符的lambda表达式(name:str->希望参数name传递的是str类型)
def getIf(name:str):
	if name=='彭兵幸':
		num=1
	else:
		num=0
	return num

print(f"getIf:{getIf('彭兵幸')}")

func4=lambda name:1 if name=='彭兵幸' else 0
print(f"func4:{func4('彭兵幸')}")