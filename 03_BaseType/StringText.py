import random

#获取图片名称和后缀(小数点分割)
photo='photo.jpg'
photoName=photo[:5]
photoEnd=photo[5:]
print(f"photoName:{photoName}\tphotoEnd:{photoEnd}")

#输入一个文件名称,求'.'的索引下标
fileName=input("输入文件名:")
position=fileName.find('.')
print(f"点的位置:{position}")

#判断某个子串是否在字符串中
fruits='apple,banana,orange,peach'
position=fruits.index('apple')
print(f"子串位置:{position}")

#生成一个6位随机验证码:包含大小写字母、数字
def generateCode(length=6):
	upperCase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	lowerCase='abcdefghijklmnopqrstuvwxyz'
	digits='0123456789'

	#合并所有字符
	allChars=upperCase+lowerCase+digits
	code=''
	for i in range(length):
		#随机选择一个索引位置
		index=random.randint(0,len(allChars)-1)
		code+=allChars[index]
	return code
print("生成5个随机验证码:")
for i in range(5):
	print(f"验证码{i+1}:{generateCode()}",end="\t")
print()
