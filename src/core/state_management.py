class QuantumStateManagement:
    def __init__(self):
        self.states = {}

    def save_state(self, node_id, state):
        """Save the quantum state of a node."""
        self.states[node_id] = state
        print(f"State saved for node {node_id}: {state}")

    def retrieve_state(self, node_id):
        """Retrieve the quantum state of a node."""
        state = self.states.get(node_id, None)
        if state is not None:
            print(f"Retrieved state for node {node_id}: {state}")
        else:
            print(f"No state found for node {node_id}")
        return state

# Example usage
if __name__ == "__main__":
    state_manager = QuantumStateManagement()
    state_manager.save_state("A", "Entangled State A")
    state_manager.retrieve_state("A")
    state_manager.retrieve_state("B")  # Should show no state found
