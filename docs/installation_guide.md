# Installation Guide

## Prerequisites
- Python 3.8 or higher
- Required libraries (listed in `requirements.txt`)

## Step-by-Step Installation
1. Clone the repository:
   ```bash
   1 git clone https://github.com/KOSASIH/Decentralized-Quantum-Internet-Core.git
   2 cd Decentralized-Quantum-Internet-Core
   ```

2. Set up a virtual environment:

   ```bash
   1 python -m venv venv
   2 source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   1 pip install -r requirements.txt
   ```
   
4. Run the setup script:

   ```bash
   1 python setup.py install
   ```
   
## Verification
To verify the installation, run the following command:

   ```bash
   1 python -m src.core.quantum_comm --version
   ```
