#!/bin/bash

# Deployment script for the Decentralized Quantum Internet Core

echo "Starting deployment..."

# Pull the latest code from the repository
git pull origin main

# Install dependencies
pip install -r requirements.txt

# Start the application (example for a finance app)
echo "Starting the finance application..."
python examples/finance_app/app.py &

# Start other applications as needed
# python examples/healthcare_app/app.py &
# python examples/secure_chat/app.py &
# python examples/voting_system/app.py &
# python examples/IoT_security/app.py &

echo "Deployment completed."
