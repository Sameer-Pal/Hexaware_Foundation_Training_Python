#  for Auth 
# models/user.py
from exception.Auth_Exceptions import AuthenticationException, AuthorizationException
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password  # In a real application, passwords should be hashed.
        self.role = role
    
    def authenticate(self, input_password):
        if self.password != input_password:
            raise AuthenticationException("Invalid password provided.")
        return True

    def authorize(self, required_role):
        if self.role != required_role:
            raise AuthorizationException(f"Access denied. Required role: {required_role}, but user role is: {self.role}.")
        return True
