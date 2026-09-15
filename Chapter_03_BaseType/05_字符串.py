#字符串使用单引号、双引号、三引号(支持换行)创建
str1='It\'s a wonderful day.'
str2="It's a wonderful day."
print(str1)
print(str2)

str3='He said "It\'s a great day."'
str4="He said \"It's a great day.\""
print(str3)
print(str4)

#字符串索引从0开始(正索引从头0、1、2开始,负索引从尾-1、-2、-3开始)
course='python'
for i in range(len(course)):
	print(course[i],end=" ")
print()

#字符串切片(列表、元组也支持):索引代表左闭右开,步长为负start从-1开始,步长可以省略(start和end的':'不能省略)
digits='0123456789'
print(f"截取范围:{digits[0:5:1]}")
print(f"截取前面:{digits[:5]}")
print(f"截取后面:{digits[5:]}")
print(f"截取所有:{digits[:]}")
print(f"截取偶数:{digits[::2]}")
print(f"反转字符:{digits[::-1]}")
#步长为正,起始和终止为负(-1代表最后一个元素)
print(f"负索引截取:{digits[-5:-1]}")
print(f"负索引截取:{digits[:-1]}")

#字符串API
str='Welcome to Python programming , Python is great.'

#1.find:检测某个子串是否包含在字符串中;存在返回子串开始的起始位置,否则返回-1
position=str.find('python')
print(f"查找子串位置:{position}")

#2.index:检测某个子串是否包含在字符串中;存在返回子串开始的起始位置,否则报异常
position=str.index('Python')
print(f"查找子串位置:{position}")

#3.replace:返回替换后的新字符串,原字符串不变(第3个参数为替换次数,默认全部替换)
str='I love C++ is interesting.'
newStr=str.replace('C++','Python')
print(f"新串替换旧串:{newStr}")

#4.split:切割后返回一个列表
date='2026-05-27-13:45:40'
dateList=date.split('-')
print(f"分割数字列表:{dateList}")

#5.join:将一个序列拼接为字符串
fruitList=['apple','banana','orange','peach']
result='-'.join(fruitList)
print(f"拼接字符序列:{result}")


