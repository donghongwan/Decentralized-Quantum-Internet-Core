import requests

class BlockchainUtils:
    @staticmethod
    def get_blockchain_data(transaction_id):
        response = requests.get(f"http://blockchain-api.local/transactions/{transaction_id}")
        return response.json() if response.status_code == 200 else None
