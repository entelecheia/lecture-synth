import jwt

from app.config import JWT_ALGORITHM, JWT_EXPIRATION_DELTA, JWT_SECRET_KEY
from datetime import datetime, timedelta, timezone
from flask import jsonify, request
from functools import wraps


def generate_token(user_id: str) -> str:
    """
    Generate a JWT token for a user.

    Args:
        user_id (str): The ID of the user.

    Returns:
        str: The generated JWT token.
    """
    try:
        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(days=JWT_EXPIRATION_DELTA),
            "iat": datetime.now(timezone.utc),
            "sub": user_id,
        }
        return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    except Exception as e:
        return str(e)


def decode_token(token: str) -> dict:
    """
    Decode a JWT token.

    Args:
        token (str): The JWT token to decode.

    Returns:
        dict: The decoded token payload.
    """
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError as e:
        raise jwt.ExpiredSignatureError("Token has expired") from e
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError("Invalid token")


def token_required(f):
    """
    Decorator to protect routes that require authentication.
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({"message": "Token is missing"}), 401

        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            payload = decode_token(token)
            current_user = payload["sub"]
        except Exception as e:
            return jsonify({"message": str(e)}), 401

        return f(current_user, *args, **kwargs)

    return decorated


def is_token_valid(token: str) -> bool:
    """
    Check if a token is valid.

    Args:
        token (str): The JWT token to validate.

    Returns:
        bool: True if the token is valid, False otherwise.
    """
    try:
        decode_token(token)
        return True
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return False
