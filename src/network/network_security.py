import hashlib

class NetworkSecurity:
    def __init__(self):
        self.encryption_key = "super_secret_key"

    def encrypt(self, message):
        """Encrypt a message using a simple hash function."""
        encrypted_message = hashlib.sha256((message + self.encryption_key).encode()).hexdigest()
        print(f"Encrypted message: {encrypted_message}")
        return encrypted_message

    def decrypt(self, encrypted_message):
        """Decrypt the message (placeholder, as hashing is one-way)."""
        print("Decryption not possible with hash functions.")
        return None

    def authenticate(self, node_id, signature):
        """Authenticate a node using a simple signature check."""
        expected_signature = self.generate_signature(node_id)
        is_authenticated = expected_signature == signature
        print(f"Node {node_id} authentication status: {is_authenticated}")
        return is_authenticated

    def generate_signature(self, node_id):
        """Generate a signature for a node."""
        return hashlib.sha256((node_id + self.encryption_key).encode()).hexdigest()

# Example usage
if __name__ == "__main__":
    security = NetworkSecurity()
    message = "Hello, secure world!"
    encrypted_message = security.encrypt(message)

    node_id = "NodeA"
    signature = security.generate_signature(node_id)
    security.authenticate(node_id, signature)
