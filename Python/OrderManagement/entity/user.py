# 5. Create a User class with attributes:

class User:
    def __init__(self, username, password, role, userId=None):
        self._userId = userId
        self._username = username
        self._password = password
        self._role = role

    # Getter for userId
    @property
    def userId(self):
        return self._userId

    # Setter for userId
    @userId.setter
    def userId(self, value):
        self._userId = value

    # Getter for username
    @property
    def username(self):
        return self._username

    # Setter for username
    @username.setter
    def username(self, value):
        self._username = value

    # Getter for password
    @property
    def password(self):
        return self._password

    # Setter for password
    @password.setter
    def password(self, value):
        self._password = value

    # Getter for role
    @property
    def role(self):
        return self._role

    # Setter for role
    @role.setter
    def role(self, value):
        self._role = value
