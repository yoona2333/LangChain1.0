from langchain.messages import HumanMessage, ToolMessage
import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv("../.env")  # 加载环境变量

# if not os.getenv("DEEPSEEK_API_KEY"):
#     raise Exception("DEEPSEEK_API_KEY 读取失败！检查.env文件位置、文件名、内容格式")

model = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_API_BASE_URL"),
)

def get_weather(city: str):


    """获取天气的工具"""
    return f"{city}天气晴朗"
# 将模型和工具绑定
model_with_tools = model.bind_tools([get_weather])
messages = [
    HumanMessage("今天北京天气如何")
]
# 模型生成调用工具请求
response = model_with_tools.invoke(messages)
# 添加AIMessage
messages.append(response)
tool_calls = response.tool_calls
for tool_call in tool_calls:
    if tool_call["name"] == "get_weather":
# 拼接出ToolMessage实例
        tool_response = ToolMessage(
            content=get_weather(**tool_call["args"]),
            tool_call_id=tool_call["id"],
            name=tool_call["name"]
        )
messages.append(tool_response)

print("=====================> messages <=====================")
for msg in messages:
    msg.pretty_print()
print("=====================> messages <=====================")
final_response = model_with_tools.invoke(messages)
print(f"final_response: \n{final_response}")
