class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
