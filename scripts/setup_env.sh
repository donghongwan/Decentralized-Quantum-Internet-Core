#!/bin/bash

# Environment setup script for the Decentralized Quantum Internet Core

echo "Setting up the environment..."

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

echo "Environment setup completed. Activate the environment using 'source venv/bin/activate'."
