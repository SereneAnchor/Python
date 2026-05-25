#案例1:给定一个字符串,以字典的形式统计每个字符出现的次数(如果key存在则修改对应的值,如果key不存在则新增该键值对)
print("======== 案例1 ========")
str1="acsjbgfdauksfhjksahlksjd"
resultDict1={}
for ch in str1:
	if ch in resultDict1.keys():
		resultDict1[ch]+=1
	else:
		resultDict1[ch]=1
print(f"resultDict1:{resultDict1}")

#案例2:将字符串转为字典(8=Eight 9=Nine 10=Ten->{'8':'Eight','9':'Nine','10':'Ten'})
print("======== 案例2 ========")
str2='8=Eight 9=Nine 10=Ten'

#使用split根据空格划分子串返回一个列表,列表中每个元素都是字符串
resultList2=str2.split(' ')
resultDict2={}
print(f"resultList2:{resultList2}")

#对每个字符串根据'='来进行拆包处理(列表、元组的拆包简单,字符串的拆包要结合split方法使用返回一个列表)
for item in resultList2:
	key,value=item.split('=')
	resultDict2[key]=value
print(f"resultDict2:{resultDict2}")


