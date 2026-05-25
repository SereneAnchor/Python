#lambda表达式为匿名函数

#1.普通函数
def getStr(str):
	return 'Hello '+str

print(getStr('Python'))

fn1=lambda str:'Hello '+str
print(fn1('C++'))

#2.带参数的lambda表达式
fn2=lambda num1,num2:num1+num2
print(f"fn2:{fn2(2,3)}")

#3.带默认参数的lambda表达式(默认参数必须在右侧)
fn3=lambda num1,num2=20:num1+num2
print(f"fn3:{fn3(10)}")

#4.带if/三目运算符的lambda表达式(name:str->希望参数name传递的是str类型)
def getIf(name:str):
	if name=='彭兵幸':
		num=1
	else:
		num=0
	return num
print(getIf('彭兵幸'))

fn4=lambda name:1 if name=='彭兵幸' else 0
print(f"fn4:{fn4('彭兵幸')}")