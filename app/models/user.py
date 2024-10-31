# app/models/user.py

import uuid
import boto3
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils.config import get_dynamodb_client

dynamodb = get_dynamodb_client()
table = dynamodb.Table('Users')


class User:
    @staticmethod
    def create_user(username, password):
        hashed_password = generate_password_hash(password)
        user_id = str(uuid.uuid4())
        table.put_item(
            Item={
                "user_id": user_id,
                "username": username,
                "password": hashed_password
            }
        )

    @staticmethod
    def get_user(username):
        response = table.get_item(Key={"username": username})
        return response.get("Item")

    @staticmethod
    def verify_password(stored_password, provided_password):
        return check_password_hash(stored_password, provided_password)
