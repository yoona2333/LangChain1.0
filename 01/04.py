# 1. **`format_messages()`**：填充模板变量，**直接返回 `list[BaseMessage]`**（`[SystemMessage,HumanMessage,...]`），只做渲染，**不调用大模型**Langchain
# 2. **`format()`**：填充模板变量，返回**拼接好的纯文本字符串**，老式单文本提示词用，**不调用大模型**Langchain
# 3. **`invoke()`**（模板的 invoke，不是 model.invoke！这点最容易混淆）：填充变量，返回 **ChatPromptValue**（包装好的消息容器，可直接丢进模型），**不调用大模型**LangChain
#
# >
# > ⚠️ 重点区分两个完全不同的 invoke：
# >
# >
# > - `prompt_template.invoke()`：**模板渲染，只是组装消息，不请求 API**
# > - `model.invoke()`：**真正把消息发给大模型 API，向云端请求，返回 AIMessage**
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

chat_prompt_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="我是一个贴心的智能助手"),
    HumanMessage(content="我的问题是:人工智能英文怎么说？")
])
messages = chat_prompt_template.invoke({})
print(messages)
print(type(messages))

# messages=[SystemMessage(content='我是一个贴心的智能助手', additional_kwargs={},
# response_metadata={}), HumanMessage(content='我的问题是:人工智能英文怎么说？',
# additional_kwargs={}, response_metadata={})]
# <class 'langchain_core.prompt_values.ChatPromptValue'>

# 注意：在XxxMessage中不能有占位符。即：不能在XxxMessage中使用{variable_name}占位符。
# messages=[SystemMessage(content='我是一个贴心的智能助手', additional_kwargs=
# {}, response_metadata={}), HumanMessage(content='我的问题是:{word}英文怎么
# 说？', additional_kwargs={}, response_metadata={})]
# <class 'langchain_core.prompt_values.ChatPromptValue'>


chat_prompt_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="我是一个贴心的智能助手"),
    HumanMessage(content="我的问题是:{word}英文怎么说？")
])
messages = chat_prompt_template.invoke({"word": "人工智能"})
print(messages)
print(type(messages))

# HumanMessagePromptTemplate，专用于生成 用户消息（HumanMessage） 的模板类
# 模板化 ：支持使用变量占位符，可以在运行时填充具体值
# 格式化 ：能够将模板与输入变量结合生成最终的聊天消息
# 输出类型 ：生成 HumanMessage 对象（ content + role="human" ）
# 设计目的 ：简化用户输入消息的模板化构造，避免重复定义角色
# SystemMessagePromptTemplate、AIMessagePromptTemplate：类似于以上模板类，用于生成系统消息和助手消息




# 导入聊天消息类模板
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

# 创建消息模板
# 创建消息模板
system_message_prompt = SystemMessagePromptTemplate.from_template("你是一个{role}")
human_message_prompt = HumanMessagePromptTemplate.from_template("给我解释{concept}，用浅显易懂的语言")
# 组合成聊天提示模板
chat_prompt = ChatPromptTemplate.from_messages([
    system_message_prompt,
    human_message_prompt
])
# 格式化提示
formatted_messages = chat_prompt.invoke({"role": "物理学家", "concept": "相对论"})
print(formatted_messages)
