from cryptography.fernet import Fernet

class Encryption:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, plaintext):
        """Encrypt a plaintext message."""
        encrypted = self.cipher.encrypt(plaintext.encode())
        return encrypted

    def decrypt(self, encrypted):
        """Decrypt an encrypted message."""
        decrypted = self.cipher.decrypt(encrypted).decode()
        return decrypted

# Example usage
if __name__ == "__main__":
    encryption = Encryption()
    message = "Hello, secure world!"
    encrypted_message = encryption.encrypt(message)
    print(f"Encrypted: {encrypted_message}")
    decrypted_message = encryption.decrypt(encrypted_message)
    print(f"Decrypted: {decrypted_message}")
