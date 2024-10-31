from app.models.user import User
from app.utils.helpers import generate_token, verify_token

class AuthService:
    @staticmethod
    def register_user(username, password):
        if User.get_user(username):
            raise ValueError("User already exists")
        User.create_user(username, password)
        return {"message": "User registered successfully"}

    @staticmethod
    def login_user(username, password):
        user = User.get_user(username)
        if user and User.verify_password(user["password"], password):
            token = generate_token(username)
            return {"token": token}
        raise ValueError("Invalid username or password")

    @staticmethod
    def authenticate(token):
        user_id = verify_token(token)
        if not user_id:
            raise ValueError("Invalid or expired token")
        return user_id
