import ollama

MODEL_NAME='deepseek-r1:1.5b'


def buildErrorMessage(error):
	errorText=str(error)
	errorTextLower=errorText.lower()

	if 'connection refused' in errorTextLower or 'failed to connect' in errorTextLower:
		return 'Ollama 服务连接失败,请确认本地 Ollama 已启动.'
	if 'model' in errorTextLower and (
			'not found' in errorTextLower or 'does not exist' in errorTextLower):
		return f'未找到模型 {MODEL_NAME},请先执行: ollama pull {MODEL_NAME}'
	if 'timed out' in errorTextLower or 'timeout' in errorTextLower:
		return 'Ollama 请求超时,请稍后重试或检查模型是否正在加载.'

	return f'调用 Ollama 时发生异常:{errorText}'


def Chat(messages):
	try:
		response=ollama.chat(model=MODEL_NAME,messages=messages)
		return response['message']['content']
	except ollama.ResponseError as error:
		return buildErrorMessage(error)
	except Exception as error:
		return buildErrorMessage(error)


def getResponse(prompt):
	return Chat([{'role':'user','content':prompt}])


def getResponseList(promptList):
	return Chat(promptList[-20:])


messageList=[{'role':'user','content':'你好,学习AI有什么方式吗?请给我5条学习建议,每条不超过30字.'}]

#直接执行当前文件时,执行测试语句;当前文件被导入时不执行测试语句
if __name__=='__main__':
	print(getResponseList(messageList))
