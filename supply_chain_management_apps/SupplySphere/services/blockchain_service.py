import requests

class BlockchainService:
    @staticmethod
    def record_transaction(data):
        response = requests.post("http://blockchain-api.local/transactions", json=data)
        return response.json() if response.status_code == 200 else None
