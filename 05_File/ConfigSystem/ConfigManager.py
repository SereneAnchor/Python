import os
import json


#加载配置文件
def loadConfig(fileName):
	try:
		with open(fileName,'r',encoding='utf-8') as file:
			#将JSON文件内的内容转为字典
			config=json.load(file)
		print(f"配置已加载:{fileName}")
		return config
	except FileNotFoundError:
		print(f"错误:配置文件不存在-{fileName}")
		return {}
	except json.JSONDecodeError:
		print(f"错误:配置文件格式错误-{fileName}")
		return {}

#保存配置文件
def saveConfig(fileName,config):
	try:
		with open(fileName,'w',encoding='utf-8') as file:
			#写入配置信息到配置文件
			json.dump(config,file,indent=4,ensure_ascii=False)
		print(f"配置已保存:{fileName}")
		return True
	except IOError as error:
		print(f"错误:保存配置失败-{error}")
		return False

#获取配置值
def getConfigValue(config,key,default=None):
	#config是一个字典,get方法根据键返回值,key不存在get方法返回默认值None(如果使用config[key]会报错)
	return config.get(key,default)

#设置配置值
def setConfigValue(config,key,value):
	config[key]=value
	return config

#主函数
def main():
	configFile='config.json'

	#加载配置
	config=loadConfig(configFile)

	#d当前目录没有config.json时,config为空字典,写入初始配置
	if not config:
		config={'appName':'MyApp','version':'1.0.0','debug':True,'port':8000}
		saveConfig(configFile,config)

	#获取配置值
	appName=getConfigValue(config,'appName')
	print(f"应用名称:{appName}")

	#修改配置
	config=setConfigValue(config,'debug',False)
	saveConfig(configFile,config)

#只有当前py文件执行时,才执行main;如果main被别的文件import导入,就不会自动执行main方法
if __name__=='__main__':
	main()







