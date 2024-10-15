


# exceptions/authorization_exception.py
class AuthorizationException(Exception):
    def __init__(self, message="User not authorized"):
        super().__init__(message)

# exceptions/authentication_exception.py
class AuthenticationException(Exception):
    def __init__(self, message="User not authenticated"):
        super().__init__(message)



