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