"""
Supervisor Agent for Adapter Testing using LangGraph
This script adds a true supervisor agent that:
- Discovers all adapter test agents
- Triggers each agent
- Monitors results
- Makes decisions (e.g., retry on failure, summary reporting)
"""
import importlib
import os
from langgraph.graph import StateGraph
from langgraph.constants import START, END
from langgraph.prebuilt import ToolNode
from langchain.tools import tool

ADAPTERS_MODULE = "app.adapters.test_adapters"
adapters_mod = importlib.import_module(ADAPTERS_MODULE)

test_funcs = [
    (name, func)
    for name, func in vars(adapters_mod).items()
    if callable(func) and name.startswith("test_") and name != "test_orchestrator_adapter"
]

results = {}

# Create a LangChain tool for each test function
adapter_tools = []


import types
def make_tool_factory(f, n):
    def tool_func():
        """Tool for testing adapter: {}""".format(n)
        try:
            f()
            results[n] = "success"
            return f"{n} completed successfully."
        except Exception as e:
            results[n] = f"failed: {e}"
            return f"{n} failed: {e}"
    tool_func.__name__ = f"tool_{n}"
    tool_func.__doc__ = f"Tool for testing adapter: {n}"
    return tool_func

for name, func in test_funcs:
    adapter_tools.append(make_tool_factory(func, name))

# Supervisor agent logic
def supervisor_agent(state):
    """Supervisor agent to coordinate adapter tests."""
    supervisor_agent.name = "supervisor_agent"
    supervisor_agent.description = "Supervisor agent to coordinate adapter tests."
    print("Supervisor agent starting adapter tests...")
    for tool in adapter_tools:
        print(f"Triggering {tool.__name__}...")
        result = tool()
        print(result)
    print("All adapter tests triggered. Supervisor compiling results...")
    failed = {k: v for k, v in results.items() if v != "success"}
    if failed:
        print(f"Failures detected: {failed}")
        # Decision logic: retry failed tests once
        for name in failed:
            print(f"Retrying {name}...")
            for tool in adapter_tools:
                if tool.__name__ == f"tool_{name}":
                    try:
                        tool()
                        if results[name] == "success":
                            print(f"{name} succeeded on retry.")
                        else:
                            print(f"{name} still failed: {results[name]}")
                    except Exception as e:
                        print(f"{name} retry failed: {e}")
    else:
        print("All adapter tests passed.")
    print("Supervisor agent finished.")
    return results



# Build the LangGraph with supervisor as entry point
graph = StateGraph(dict)
graph.add_node("supervisor", supervisor_agent)
graph.add_edge("supervisor", END)
graph.add_edge(START, "supervisor")
agent = graph.compile()

if __name__ == "__main__":
    print("Running Supervisor Agentic AI to test all adapters...")
    agent.invoke({})
    print("Supervisor Agentic AI completed.")
