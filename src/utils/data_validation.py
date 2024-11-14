import re

class DataValidation:
    @staticmethod
    def validate_email(email):
        """Validate an email address."""
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_ip(ip):
        """Validate an IP address."""
        pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1, 3}$'
        return re.match(pattern, ip) is not None

    @staticmethod
    def validate_integer(value):
        """Validate if the value is an integer."""
        return isinstance(value, int)

# Example usage
if __name__ == "__main__":
    email = "test@example.com"
    ip = "192.168.1.1"
    integer_value = 42

    print(f"Is '{email}' a valid email? {DataValidation.validate_email(email)}")
    print(f"Is '{ip}' a valid IP? {DataValidation.validate_ip(ip)}")
    print(f"Is '{integer_value}' a valid integer? {DataValidation.validate_integer(integer_value)}")
