#1、简易成绩管理系统:输入学生姓名和三门科目成绩、计算总分平均分、根据平均分进行评级、格式化输出所有信息
name=input("输入学生姓名:")
score1=int(input("输入科目一成绩:"))
score2=int(input("输入科目二成绩:"))
score3=int(input("输入科目三成绩:"))
sumScore=score1+score2+score3
averageScore=sumScore/3

if averageScore>=80:
	grade='A'
elif 60<=averageScore<80:
	grade='B'
elif averageScore<60:
	grade='C'

print(f"姓名:{name} 科目一:{score1} 科目二:{score2} 科目三:{score3} 总分:{sumScore} "
	  f"平均分:{averageScore:.2f} 评级:{grade}")
print("姓名:{} 科目一:{} 科目二:{} 科目三:{} 总分:{} 平均分:{:.2f} 评级:{}"
	  .format(name,score1,score2,score3,sumScore,averageScore,grade))


#2、活动费用分摊系统:输入参与人数和活动总花费、额外收取10%的管理费、计算最终总费用、判断人数是否合理、计算没人均摊费用并格式化输出
person=int(input("输入参与人数:"))
cost=float(input("输入活动费用:"))

if person<1:
	print("人数不合理.")
else:
	extraCost=cost*0.1
	sumCost=extraCost+cost
	averageCost=sumCost/person
	print(f"人数:{person} 活动花费:{cost:.2f} 管理费:{extraCost:.2f} 总费用:{sumCost:.2f} 人均费用:{averageCost:.2f}")
	print("人数:{} 活动花费:{:.2f} 管理费:{:.2f} 总费用:{:.2f} 人均费用:{:.2f}"
		  .format(person,cost,extraCost,sumCost,averageCost))

