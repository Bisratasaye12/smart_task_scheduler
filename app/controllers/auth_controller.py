from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService
from app.utils.helpers import validate_request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
@validate_request(['username','password'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    try:
        result = AuthService.register_user(username, password)
        return jsonify(result), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@auth_bp.route('/login', methods=['POST'])
@validate_request(['username', "password"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    try:
        result = AuthService.login_user(username, password)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@auth_bp.route('/verify', methods=['GET'])
def verify():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token required"}), 400

    try:
        user_id = AuthService.authenticate(token)
        return jsonify({"user_id": user_id}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
