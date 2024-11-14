# API Reference

## Overview
This document provides a detailed reference for the APIs available in the Decentralized Quantum Internet Core.

## Core Modules
### Quantum Communication
- **send(message: str)**
  - Sends a quantum message to the specified node.
  
- **receive()**
  - Receives a quantum message.

### Entanglement Management
- **create(nodes: List[str])**
  - Creates entangled states between specified nodes.

### Quantum Key Distribution
- **exchange(nodes: List[str])**
  - Initiates a quantum key exchange between specified nodes.

## Error Handling
- **QuantumError**: Raised for errors related to quantum operations.
