import streamlit as st
import ChatUtils

#页面配置
st.set_page_config(page_title='聊天机器人',page_icon='欠着',layout='wide')

#页面标题
st.title('🤖 挽挽而安的AI助手')
st.markdown('### 核心功能')
st.divider()

#核心部分
st.header('💬 AI 对话窗口')

#st.session_state是一个大字典,包含键值对:messages:[],[]内部存放多个字典(用户与AI的对话记录)
if 'messages' not in st.session_state:
	welcome={'role':'assistant','content':'你好,我是挽挽而安的助手,有什么可以帮助你的吗?'}
	st.session_state['messages']=[welcome]

#刷新之前的聊天记录
for data in st.session_state['messages']:
	with st.chat_message(data['role']):
		st.markdown(data['content'])

userInput=st.chat_input('输入问题...')

if userInput:
	#添加用户询问信息
	userMessage={'role':'user','content':userInput}
	st.session_state['messages'].append(userMessage)
	#将用户文本显示在窗口中
	st.chat_message('user').markdown(userInput)

	#调用大模型获取答案
	responseText=ChatUtils.getResponseList(st.session_state['messages'])
	dpMessage={'role':'assistant','content':responseText}
	st.session_state['messages'].append(dpMessage)
	st.chat_message('assistant').markdown(responseText)
