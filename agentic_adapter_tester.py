"""
Agentic AI Orchestrator for Adapter Testing using LangGraph
This script builds a LangGraph agent that sequentially or in parallel tests all 47 adapters in the framework, ensuring full coverage.
"""
import importlib
import os
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain.tools import tool

# Dynamically discover all adapter test functions
ADAPTERS_DIR = os.path.dirname(__file__)
ADAPTERS_MODULE = "app.adapters.test_adapters"

# Import the test_adapters module
adapters_mod = importlib.import_module(ADAPTERS_MODULE)

# Collect all test functions for adapters (excluding orchestrator)
test_funcs = [
    (name, func)
    for name, func in vars(adapters_mod).items()
    if callable(func) and name.startswith("test_") and name != "test_orchestrator_adapter"
]

# Create a LangChain tool for each test function
adapter_tools = []
for name, func in test_funcs:
    @tool(name=name, description=f"Test for {name}")
    def make_tool(f=func):
        f()
        return f"{f.__name__} completed."
    adapter_tools.append(make_tool)

# Build the LangGraph agent
with StateGraph() as graph:
    for tool in adapter_tools:
        node = ToolNode(tool)
        graph.add_node(node)
        graph.add_edge(node, END)

agent = graph.compile()

if __name__ == "__main__":
    print("Running Agentic AI to test all adapters...")
    agent.run()
    print("All adapter tests completed via Agentic AI.")
