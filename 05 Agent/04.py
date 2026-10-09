from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()
# 1. 创建 Agent 时添加 checkpointer
agent = create_agent(
    model=model,
    checkpointer=checkpointer  # 添加内存管理
)
# 2. 调用时指定 thread_id
config = {
    "configurable": {
        "thread_id": "1"
    }
}
print("\n第一轮对话：")
response1 = agent.invoke({
    "messages": [HumanMessage("我叫张三")]},
    config=config  # 传入 config
)
print(f"Agent: {response1['messages'][-1].content}")
print("\n第二轮对话：")
response2 = agent.invoke({
    "messages": [HumanMessage("我叫什么？")]},
    config=config  # 使用相同的 thread_id
)
print(f"Agent: {response2['messages'][-1].content}")
