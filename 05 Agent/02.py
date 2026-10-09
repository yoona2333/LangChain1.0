from langchain.agents import create_agent
from langchain.agents.middleware import before_model, after_model,AgentState
from langchain.messages import HumanMessage
from langgraph.runtime import Runtime
from loguru import logger
from typing import Any


def create_audit_middleware(logger):


    @before_model
    def before_log(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        logger.info("调用模型前消息数量: {}", len(state["messages"]))
    return None


@after_model
def after_log(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        logger.info("调用模型后消息数量：{}", len(state["messages"]))
        return None

    return [before_log, after_log]

agent = create_agent(
    model=model,
    middleware=[*create_audit_middleware(logger=logger)],
)
response = agent.invoke({
    "messages": [HumanMessage("你好~")]
})
for msg in response["messages"]:
    msg.pretty_print()
