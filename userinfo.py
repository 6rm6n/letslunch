import bcrypt

class UserInfo:
    def __init__(self, email, username, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)

    def hash_password(self, password):
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password.decode()  # Convert bytes to string

    def verify_password(self, input_password):
        # Verify the input password against the stored hashed password
        return bcrypt.checkpw(input_password.encode(), self.password.encode())
