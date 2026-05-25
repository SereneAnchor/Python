#1.函数内部多个return(只执行第一个return)
def getNum1():
	return 1
	return 2

print(f"getNum1():{getNum1()}")

#2.函数要返回多个值,该如何返回(以元组的形式返回)
def getNum2():
	return 1,2
print(f"getNum2():{getNum2()}")
print(f"type:{type(getNum2())}")

#3.函数位置参数
def getUser1(name,age):
	print(f"getUser1 name:{name}\tage:{age}")
getUser1('彭兵幸',10)

#4.函数关键词参数
def getUser2(name,age):
	print(f"getUser2 name:{name}\tage:{age}")
getUser2(name='彭兵幸',age=20)

#5.函数定义时缺省参数(参数默认值,缺省的参数必须写在参数列表最右侧)
def getUser3(name,age,sex='男'):
	print(f"getUser3 name:{name}\tage:{age}\tsex:{sex}")
getUser3('彭兵幸',30)
getUser3(name='彭兵幸',age=30)
getUser3(name='彭兵幸',age=30,sex='女')

#6.不定长参数(可变参数,传递的实参数量必须>=实际输出的数量)
#不定长元组(位置)参数
def getUser4(*args):
	print(f"getUser4 type:{type(args)}")
	print(f"getUser4 name:{args[0]}\tage:{args[1]}\tsex:{args[2]}")
getUser4('彭兵幸',40,'男')

#不定长字典(关键字,kw表示keyword)参数,必须使用关键词传参
def getUser5(**kwargs):
	print(f"getUser5 type:{type(kwargs)}")
	print(f"getUser5 name:{kwargs['name']}\tage:{kwargs['age']}\tsex:{kwargs['sex']}")
getUser5(name='彭兵幸',age=50,sex='女')
#传参的过程中都是一个组包的过程,组包就是把多个数据组成元组或者字典的过程

#7.args+kwargs:把元组/列表传递给args加一个*,把字典传递给kwargs加两个**
def getAK(*args,**kwargs):
	print(f"type1:{type(args)}\ttype2:{type(kwargs)}")
	print(args,end='\t')
	print(kwargs)
tuple=(10,20,30)
list=[10,20,30]
dict={'first':'A','second':'B','third':'C'}
getAK(*tuple,**dict)
getAK(*list,**dict)