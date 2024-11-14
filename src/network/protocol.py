class Protocol:
    def __init__(self):
        self.protocols = {}

    def register_protocol(self, name, handler):
        """Register a new communication protocol."""
        self.protocols[name] = handler
        print(f"Protocol registered: {name}")

    def send(self, protocol_name, message, sender, recipient):
        """Send a message using the specified protocol."""
        if protocol_name in self.protocols:
            print(f"Using protocol: {protocol_name}")
            self.protocols[protocol_name](message, sender, recipient)
        else:
            print(f"Protocol {protocol_name} not found")

# Example protocol handler
def simple_protocol(message, sender, recipient):
    print(f"{sender.node_id} (via Simple Protocol) sending: {message}")
    recipient.receive_message(message)

# Example usage
if __name__ == "__main__":
    protocol_manager = Protocol()
    protocol_manager.register_protocol("simple", simple_protocol)

    node_a = Node("A")
    node_b = Node("B")
    protocol_manager.send("simple", "Hello, Node B!", node_a, node_b)
