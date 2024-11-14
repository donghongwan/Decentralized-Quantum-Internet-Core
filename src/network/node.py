class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.connected_nodes = []
        self.state = None

    def connect(self, other_node):
        """Connect to another node."""
        if other_node not in self.connected_nodes:
            self.connected_nodes.append(other_node)
            other_node.connected_nodes.append(self)
            print(f"Node {self.node_id} connected to {other_node.node_id}")

    def send_message(self, message, recipient):
        """Send a message to a connected node."""
        if recipient in self.connected_nodes:
            print(f"Node {self.node_id} sending message to {recipient.node_id}: {message}")
            recipient.receive_message(message)
        else:
            print(f"Node {self.node_id} cannot send message to {recipient.node_id}: Not connected")

    def receive_message(self, message):
        """Receive a message from another node."""
        print(f"Node {self.node_id} received message: {message}")

# Example usage
if __name__ == "__main__":
    node_a = Node("A")
    node_b = Node("B")
    node_a.connect(node_b)
    node_a.send_message("Hello, Node B!", node_b)
