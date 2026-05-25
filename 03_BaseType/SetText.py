#案例1:给定连续递增的整数列表,找出中断的位置
print("======== 案例1 ========")

#案例2:找出数组中出现奇数次的数字
print("======== 案例2 ========")


#案例3:统计每个数字出现的次数(去重后排序),并按数字大小排序输出
print("======== 案例3 ========")
list=[4,2,2,8,3,3,1,4,3]
maxValue=max(list)
countList=[0*ele for ele in list]


#案例4:判断列表中的数组是否能组成连续序列
print("======== 案例4 ========")
list1=[4,2,3,1]
list2=[5,2,6,3]
maxValue=max(list1)
minValue=min(list1)
orderList=[ele for ele in range(minValue,maxValue+1)]
delta=maxValue-minValue+1
if delta!=len(list1):
	print(f"list1:{False}")
else:
	resultList=[ele for ele in list1 if ele in orderList]
	print(f"resultList:{resultList}")


#案例5:给定一个1到n的数组,但缺少了一些数字,找出这些缺少的数字
print("======== 案例5 ========")
randomList=[4,3,2,7,8,2,3,1]
maxValue=max(randomList)
orderList=[ele for ele in range(1,maxValue+1)]
print(f"orderList:{orderList}")
#使用列表查询:效率更慢,顺序查找
resultList1=[ele for ele in orderList if ele not in randomList]
print(f"resultList1:{resultList1}")
#使用集合查询:效率更快,哈希表查找
orderSet=set(orderList)
resultList2=[ele for ele in orderSet if ele not in randomList]
print(f"resultList2:{resultList2}")