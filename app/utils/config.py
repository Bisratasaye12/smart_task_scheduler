import boto3
import os

def get_dynamodb_client():
    return boto3.resource(
        'dynamodb',
        region_name='us-west-2',  
        endpoint_url='http://localhost:8000',
        aws_access_key_id='123456789',  
        aws_secret_access_key='123456789'
    )


# app/utils/config.py
JWT_SECRET = os.getenv("JWT_SECRET", "your_jwt_secret_key")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_SECONDS = 3600
