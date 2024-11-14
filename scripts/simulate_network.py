import random
import time

class QuantumNode:
    def __init__(self, node_id):
        self.node_id = node_id

    def send_message(self, message):
        """Simulate sending a message to another node."""
        print(f"Node {self.node_id} sending message: {message}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate network delay
        print(f"Node {self.node_id} message sent.")

def simulate_network(nodes, message):
    """Simulate a network of quantum nodes."""
    for node in nodes:
        node.send_message(message)

if __name__ == "__main__":
    nodes = [QuantumNode(i) for i in range(5)]  # Create 5 quantum nodes
    simulate_network(nodes, "Hello, Quantum Network!")
