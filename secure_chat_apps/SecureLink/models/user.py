class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
