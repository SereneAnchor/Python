import os
from datetime import datetime

def createLogFile(logDir='Logs'):
	#创建日志记录
	if not os.path.exists(logDir):
		os.makedirs(logDir)
	return logDir

def writeLogs(data,logDir='Logs',level='INFO'):
	#写入日志
	try:
		#创建日志记录
		createLogFile(logDir)

		#生成日志文件名
		today=datetime.now().strftime('%Y-%m-%d')
		logFile=os.path.join(logDir,f'{today}.log')

		#生成日志内容
		timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		logContent=f"[{timestamp}] [{level}] {data}\n"

		#写入日志
		with open(logFile,'a',encoding='utf-8') as file:
			file.write(logContent)
		print(f"日志记录:{logContent.strip()}")
	except IOError as error:
		print(f"错误:写入日志失败-{error}")

def readLogs(logDir='Logs',date=None):
	#读取日志
	try:
		if date is None:
			date=datetime.now().strftime('%Y-%m-%d')
		logFile=os.path.join(logDir,f'{date}.log')

		if not os.path.exists(logFile):
			print(f"日志文件不存在:{logFile}")
			return []
		with open(logFile,'r',encoding='utf-8') as file:
			logs=file.readlines()
		return logs
	except IOError as error:
		print(f"错误:读取日志失败-{error}")
		return []

def main():
	#写入日志
	writeLogs("程序启动",level='INFO')
	writeLogs("开始处理数据",level='INFO')
	try:
		#模拟处理
		result=10/0
	except ZeroDivisionError:
		writeLogs("发生错误:除以0",level='ERROR')
	writeLogs("程序结束",level='INFO')

	#读取日志
	logs=readLogs()
	print(f"\n今日日志:")
	for log in logs:
		print(log.strip())

if __name__=='__main__':
	main()



