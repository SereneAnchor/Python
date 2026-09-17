#处理JSON文件

import json
def readJSON(fileName):
	with open(fileName,'r',encoding='utf-8') as file:
		#从打开的json文件中读取内容并转换为Python数据(字典)
		data=json.load(file)
	return data

def writeJSON(fileName,data):
	with open(fileName,'w',encoding='utf-8') as file:
		#indent表示缩进4个空格,控制中文的显示格式(非乱码)
		json.dump(data,file,indent=4,ensure_ascii=False)

student={"name":"张三","sex":"男","age":18,"hobbies":["Python","篮球","音乐"]}

#写入JSON文件
writeJSON('Student.json',student)

#读取JSON文件
result=readJSON('Student.json')

#打印读取结果
print(result)
