# Usage Guide

## Overview
This guide provides instructions on how to use the Decentralized Quantum Internet Core for various applications.

## Basic Usage
1. **Starting a Node**:
   ```bash
   python -m src.network.node --start
   ```

2. Sending a Quantum Message:

   ```bash
   1 python -m src.core.quantum_comm --send --message "Hello, Quantum World!"
   ```
   
## Advanced Features

- **Entanglement Creation**:

   ```bash
   1 python -m src.core.entanglement --create --nodes <node_ids>
   ```
   
- **Quantum Key Distribution**:

   ```bash
   1 python -m src.core.qkd --exchange --nodes <node_ids>
   ```
   
## Conclusion
Refer to the API documentation for more advanced usage and options.
