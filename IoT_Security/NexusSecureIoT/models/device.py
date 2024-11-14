class Device:
    def __init__(self, device_id, device_type, owner):
        self.device_id = device_id
        self.device_type = device_type
        self.owner = owner
        self.status = "offline"
