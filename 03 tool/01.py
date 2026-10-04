from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """
    获取指定城市的天气信息
    参数:
    city: 城市名称，如"北京"、"上海"
    返回:
    天气信息字符串
    """
# 你的实现
    return city + "晴天，温度 15°C"


print(get_weather.invoke({"city": "北京"}))

# ⚠️ **普通函数调用：`get_weather("北京")`，直接传位置参数**
# ⚠️ **Tool 对象的 invoke：必须传字典，key 对应参数名 `{"city":"北京"}`**

