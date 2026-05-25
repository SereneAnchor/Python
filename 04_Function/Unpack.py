#1.元组拆包:把元组中的数据一个一个拆解出来,用多个变量接收元组元素

#元组拆包过程:将10、20分别赋值给num1、num2,也可以有其他写法
tuple1=(10,20)
num1,num2=tuple1
print(f"num1:{num1}\t\tnum2:{num2}")

tuple2=('Serene','Anchor')
str1,str2=('Serene','Anchor')
print(f"str1:{str1}\nstr2:{str2}")

tuple3=('S','A')
ch1,ch2='S','A'
print(f"ch1:{ch1}\t\tch2:{ch2}")

#元组拆包实现交换变量值
name1="蔡徐坤"
name2="王富贵"
name2,name1=(name1,name2)
print(f"name1:{name1}\nname2:{name2}")

print(f"====================")

#2.列表拆包
#列表拆包过程:将10、20分别赋值给num1、num2
list1=[10,20]
num1,num2=list1
print(f"num1:{num1}\t\tnum2:{num2}")

list2=['Serene','Anchor']
str1,str2=['Serene','Anchor']
print(f"str1:{str1}\nstr2:{str2}")

#元组拆包实现交换变量值
name1="蔡徐坤"
name2="王富贵"
[name2,name1]=[name1,name2]
print(f"name1:{name1}\nname2:{name2}")

#不定长拆包:将第一个元素赋值给head,剩下的所有元素打包成一个新列表赋值给tail
colors=['red','blue','green','yellow']
head,*tail=colors
print(f"head:{head}")
print(f"tail:{tail}")
