"""
  整数、浮点数、字符串(单双引号均可)、布尔值、
  列表(list,有序可变集合)、元组(tuple,有序不可变集合)、字典(dict,键值对集合)
"""
age=20
weight=68.5
str1="Python"
str2='python'
flag=True
nums=[1,2,3,4,5]
info=("张三",20)
student={"name":"李四","age":25}

#1、类型检查:type函数、isinstance函数
print(type(age))
print(isinstance(age,int))
print(isinstance(age,str))

#2.1、格式化输出:基础用法、保留两位小数(:.2f)、控制六位宽度(把数字'1'用'0'来补充到六位,以十进制整数表示)、
name='Sally'
age=30
score=87.7
print(f"姓名:{name},年龄:{age},成绩:{score}")
print(f"保留成绩两位小数:{score:.2f}")
print(f"学号:{1:06d}")

#2.2、format方法(可以通过变量在format中的索引指定变量放在字符串的哪个占位符)
print("姓名:{},年龄:{}".format(name,age))
print("年龄:{1},姓名:{0}".format(name,age))
print(f"学号:{1:06d}")

#2.3、%占位符
print("姓名:%s,年龄:%d,成绩:%.2f"%(name,age,score))

#3、转义字符:\n换行、\t制表符、\\反斜杠、\'单引号、\"双引号
print(f"姓名:{name}\t年龄:{age}\t成绩:{score}")
print("姓名:{}\t年龄:{}\t成绩:{:.2f}".format(name,age,score))

#4、自定义换行符(end参数默认值为'\n',控制print打印完内容后结尾添加什么字符,将其替换为空格表示不换行只是添加空格)
print("Hello",end=" ")
print("Python!")

#5、输入函数(从键盘输入内容,所有输入均为字符串)
name=input("请输入姓名:")
age=input("请输入年龄:")
phone=input("请输入手机号:")
print(f"姓名:{name}\t年龄:{age}")
print("姓名:{}\t年龄:{}\t".format(name,age))
print(f"手机号:{phone},类型:{type(phone)}")

#6、数据类型转换:对于输入的字符串进行数值计算时需要进行类型转换
"""
	int(x)   将x转为整数       int("100")->100
	float(x) 将x转为浮点数	     float("3.14")->3.14	
	str(x)   将x转为字符串      str(18)->"18"
	eval(x)  执行字符串表达式    eval("1+2")->3 
"""
productName=input("输入商品名称:")
productPrice=input("输入商品单价:")
productCount=input("输入商品数量:")
price=float(productPrice)
count=int(productCount)
sumPrice=price*count
print(f"购买商品:{productName} 商品单价:{price:.2f} 商品数量:{productCount} 总价:{sumPrice:.2f}")
print("购买商品:{} 商品单价:{:.2f} 商品数量:{} 总价:{:.2f}".format(productName,price,count,sumPrice))
