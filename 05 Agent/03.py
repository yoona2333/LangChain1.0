from langchain.agents import create_agent
from langchain.agents.middleware import before_model, after_model, AgentState, AgentMiddleware
from langchain.messages import HumanMessage
from langgraph.runtime import Runtime
from loguru import logger
from typing import Any


class CreateAuditMiddleware(AgentMiddleware):
    def __init__(self, logger):
        super().__init__()
        self.logger = logger


def before_model(self, state: AgentState, runtime: Runtime) -> dict[str,
Any] | None:
    self.logger.info("调用模型前消息数量: {}", len(state["messages"]))
    return None


def after_model(self, state: AgentState, runtime: Runtime) -> dict[str,
Any] | None:
    self.logger.info("调用模型后消息数量：{}", len(state["messages"]))
    return None

agent = create_agent(
    model=model,
    middleware=[CreateAuditMiddleware(logger=logger)],
)
response = agent.invoke({
    "messages": [HumanMessage("你好~")]
})
for msg in response["messages"]:
    msg.pretty_print()
