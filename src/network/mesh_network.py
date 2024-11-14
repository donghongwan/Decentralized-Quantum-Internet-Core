class MeshNetwork:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        """Add a node to the mesh network."""
        self.nodes.append(node)
        print(f"Node {node.node_id} added to the mesh network")

    def broadcast(self, message, sender):
        """Broadcast a message to all connected nodes."""
        print(f"Broadcasting message from {sender.node_id}: {message}")
        for node in self.nodes:
            if node != sender:
                node.receive_message(message)

# Example usage
```python
if __name__ == "__main__":
    mesh_network = MeshNetwork()
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")

    mesh_network.add_node(node_a)
    mesh_network.add_node(node_b)
    mesh_network.add_node(node_c)

    node_a.connect(node_b)
    node_b.connect(node_c)

    mesh_network.broadcast("Hello, everyone!", node_a)
