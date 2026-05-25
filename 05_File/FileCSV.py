#处理CSV文件
def readCSV(fileName):
	students=[]
	with open(fileName,'r',encoding='utf-8') as file:
		#跳过表头
		file.readline()
		for line in file:
			name,sex,age=line.rstrip('\n').split(',')
			students.append({'name':name,'sex':sex,'age':age})
	return students


def writeCSV(fileName,students):
	with open(fileName,'w',encoding='utf-8') as file:
		file.write('姓名,性别,年龄\n')
		for student in students:
			line=f"{student['name']},{student['sex']},{student['age']}\n"
			file.write(line)


students=[
	{'name':'张三','sex':'男','age':'18'},
	{'name':'李四','sex':'女','age':'19'},
	{'name':'王五','sex':'男','age':'20'}
]

#写入CSV文件
writeCSV('Students.csv',students)

#读取CSV文件
result=readCSV('Students.csv')

#打印读取结果
print(result)