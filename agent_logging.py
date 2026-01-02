import threading
import time
import logging
from collections import defaultdict

# Thread-safe log and metrics collector for agents
class AgentLogger:
    def __init__(self):
        self.lock = threading.Lock()
        self.logs = []
        self.metrics = defaultdict(list)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

    def log(self, agent, msg_type, message):
        entry = {
            'timestamp': time.time(),
            'agent': agent,
            'msg_type': msg_type,
            'message': message
        }
        with self.lock:
            self.logs.append(entry)
        logging.info(f"[{agent}][{msg_type}] {message}")

    def record_metric(self, agent, metric, value):
        with self.lock:
            self.metrics[agent].append((metric, value, time.time()))

    def get_logs(self):
        with self.lock:
            return list(self.logs)

    def get_metrics(self):
        with self.lock:
            return dict(self.metrics)

agent_logger = AgentLogger()
