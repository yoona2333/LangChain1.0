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


# responses=model.invoke("你好")
# print(responses.content)

# 定义工具
from langchain.tools import tool
def get_weather(city: str) -> str:
    """获取指定城市的天气"""
# 你的实现
    return "晴天，温度 15°C"


model_with_tools=model.bind_tools([get_weather])  # 绑定工具

response=model_with_tools.invoke("北京天气如何？") #**大模型自己理解句子，提取出城市 “北京”**，生成`{"city":"北京"}`参数字典

if response.tool_calls:
    print("AI 想调用工具：", response.tool_calls)
else:
    print("AI 直接回答：", response.content)
# # AI 可以决定是否调用工具
# response = model_with_tools.invoke("北京天气如何？")
# # response = model_with_tools.invoke("2 + 3 = ？")
# # 检查 AI 是否要调用工具
# if response.tool_calls:
#     print("AI 想调用工具：", response.tool_calls)
# else:
#     print("AI 直接回答：", response.content)
