import streamlit as st

#页面配置
st.set_page_config(page_title='聊天机器人',page_icon='欠着',layout='wide')

#页面标题
st.title('🤖 挽挽而安的AI助手')
st.markdown('### 核心功能')
st.divider()

#侧边栏
with st.sidebar:
	st.title('⚙️ 机器人设置')
	botName=st.text_input('机器人名称',value='智能助手')
	modelMode=st.selectbox('对话风格',['通用闲聊','专业问答','文案创作','心理咨询'])
	replyLength=st.radio('回复长度',['简短','中等','详细'])
	enableFunc=st.multiselect('附加功能',['联网搜索','代码解释','文本翻译','内容总结'])
	temperature=st.slider('AI 创意程度',min_value=0.0,max_value=1.0,value=0.6,step=0.1)
	autoClean=st.checkbox('发送后自动清空输入',value=False)

#主页面
st.header('👤 用户输入区')
leftCol,rightCol=st.columns(2)
with leftCol:
	userName=st.text_input('昵称',placeholder='请输入昵称...')
	userAge=st.number_input('年龄',min_value=0,max_value=100,value=25)

with rightCol:
	userSex=st.selectbox('性别',['男','女','保密'])
	userMood=st.slider('心情指数',0,10,5)

st.divider()

#核心部分
st.header('💬 AI 对话窗口')

#st.session_state保存聊天记录,用户每次输入、点击按钮、改变控件都会导致py文件重新执行一遍,丢失原有的聊天记录
if 'messages' not in st.session_state:
	st.session_state['messages']=[]
else:
	#刷新之前的聊天记录
	for data in st.session_state['messages']:
		with st.chat_message(data['role']):
			st.markdown(data['content'])

userInput=st.chat_input('输入问题...')
if userInput:
	#刷新输入的新内容
	st.session_state['messages'].append({'role':'user','content':userInput})
	with st.chat_message('user'):
		st.markdown(userInput)


	#模拟AI回复
	dpReply=f"""
	你好:{userName if userName else '朋友'}!
	当前心情指数:{userMood}分(满分10分)
	你发送的内容:{userInput}
	---
	 - 机器人配置
	 - 机器人名称:{botName}
	 - 对话风格:{modelMode}
	 - 回复长度:{replyLength}
	 - AI创意度:{temperature}
	 - 开启功能:{', '.join(enableFunc) if enableFunc else '无'}
	---
	提示:以上为模拟回复,替换大模型API后可实现真实API对话
	"""
	st.session_state['messages'].append({'role':'assistant','content':dpReply})
	with st.chat_message('assistant'):
		st.markdown(dpReply)

	#如果用户勾选了自动清空记录按钮,就调用rerun,等价于刷新界面
	# if autoClean:
	# 	st.rerun()

#如果用户点击了清空聊天记录按钮,那就删除聊天记录
if st.button('🔄 清空聊天记录'):
	st.session_state['messages']=[]
	st.rerun()

