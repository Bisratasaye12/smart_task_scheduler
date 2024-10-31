from functools import wraps
from flask import request, jsonify
import jwt
from datetime import datetime, timedelta
from app.utils.config import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRATION_SECONDS


def validate_request(required_fields):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.json
            for field in required_fields:
                if field not in data or not data[field]:
                    return jsonify({'error': f'Missing required field: {field}'}), 400
            return func(*args, **kwargs)
        return wrapper
    return decorator

def generate_token(user_id):
    expiration = datetime.utcnow() + timedelta(seconds=JWT_EXPIRATION_SECONDS)
    payload = {"user_id": user_id, "exp": expiration}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def verify_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
