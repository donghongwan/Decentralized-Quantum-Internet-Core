from cryptography.fernet import Fernet

class Encryption:
    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    @staticmethod
    def encrypt_data(data, key):
        fernet = Fernet(key)
        return fernet.encrypt(data.encode())

    @staticmethod
    def decrypt_data(encrypted_data, key):
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_data).decode()
