#1.覆盖写入(以'w'方式写入,就会清空原文件内容)
with open('Write.txt','w',encoding='utf-8') as file:
	file.write('覆盖第一行\n')
	file.write('覆盖第二行\n')

#2.追加(以'a'方式写入,不会覆盖原文件内容)
with open('Write.txt','a',encoding='utf-8') as file:
	file.write('追加第一行\n')

#3.print写入
with open('Write.txt','w',encoding='utf-8') as file:
	#平常使用print打印内容到屏幕,这里是写入到文件对象file内,且会自动换行
	print('print第一行',file=file)
	print('print第一行',file=file)

#4.写入列表
lines=['第一行\n','第二行\n','第三行\n']
with open('Write.txt','w',encoding='utf-8') as file:
	#把字符串列表中的每个字符依次写入文件
	file.writelines(lines)


