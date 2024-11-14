class BlockchainRecord:
    def __init__(self, record_id, device_id, action, timestamp):
        self.record_id = record_id
        self.device_id = device_id
        self.action = action
        self.timestamp = timestamp
