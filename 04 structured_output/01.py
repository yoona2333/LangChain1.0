from dataclasses import field
from urllib import response

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

from pydantic import BaseModel,Field

class Person(BaseModel):
    name:str=Field(description="姓名")
    age:int=Field(description="年龄")
    occupation:str=Field(description="职业")


# 从.env文件中加载环境变量
load_dotenv(override=True)
CLOSEAI_API_KEY = os.getenv("CLOSEAI_API_KEY")
CLOSEAI_BASE_URL = os.getenv("CLOSEAI_BASE_URL")
model = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key=CLOSEAI_API_KEY,
    base_url=CLOSEAI_BASE_URL
)
# response = model.invoke("你好")
# print(response)
print(model.with_structured_output(Person).invoke("张三是一个30岁的程序员"))
