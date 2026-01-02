import time
from agent_logging import agent_logger

def generate_sequence_diagram(logs, filename="agent_interaction_diagram.txt"):
    """
    Generates a simple text-based sequence diagram of agent interactions.
    """
    agents = set(log['agent'] for log in logs)
    agents = sorted(agents)
    agent_indices = {agent: i for i, agent in enumerate(agents)}
    lines = [f"Agents: {', '.join(agents)}\n"]
    timeline = []
    for log in logs:
        ts = time.strftime('%H:%M:%S', time.localtime(log['timestamp']))
        agent = log['agent']
        msg_type = log['msg_type']
        message = log['message']
        timeline.append((log['timestamp'], agent, msg_type, message, ts))
    timeline.sort()
    for _, agent, msg_type, message, ts in timeline:
        lines.append(f"[{ts}] {agent}: {msg_type} - {message}")
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    print(f"Sequence diagram written to {filename}")

def generate_mermaid_sequence(logs, filename="agent_interaction_mermaid.md"):
    """
    Generates a Mermaid.js sequence diagram markdown file from agent logs.
    """
    lines = ["```mermaid", "sequenceDiagram"]
    prev_agent = None
    for log in sorted(logs, key=lambda l: l['timestamp']):
        agent = log['agent']
        msg_type = log['msg_type']
        message = log['message'].replace('"', "'")
        if msg_type == 'start':
            lines.append(f"    participant {agent}")
        if prev_agent and prev_agent != agent:
            lines.append(f"    {prev_agent}->>{agent}: {msg_type} - {message}")
        else:
            lines.append(f"    Note right of {agent}: {msg_type} - {message}")
        prev_agent = agent
    lines.append("```")
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    print(f"Mermaid sequence diagram written to {filename}")

if __name__ == "__main__":
    logs = agent_logger.get_logs()
    generate_sequence_diagram(logs)
    generate_mermaid_sequence(logs)
