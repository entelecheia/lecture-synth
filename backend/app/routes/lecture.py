"""
This module contains routes related to lecture generation and management.

Routes:
- /generate_lecture (POST): Generates a lecture and slides based on the given topic and duration.
- /lectures (GET): Placeholder for retrieving previously generated lectures (not yet implemented).

Each route is protected by token-based authentication.
"""

from app.services.lecture_generator import generate_lecture_and_slides
from app.utils.auth import token_required
from flask import jsonify, request

from . import routes


@routes.route("/generate_lecture", methods=["POST"])
@token_required
def generate_lecture():
    try:
        data = request.get_json()
        topic = data.get("topic")
        duration = data.get("duration")

        if not topic or not duration:
            return jsonify({"error": "Missing topic or duration"}), 400

        result = generate_lecture_and_slides(topic, duration)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@routes.route("/lectures", methods=["GET"])
@token_required
def get_lectures():
    # This is a placeholder for a potential future feature
    # to retrieve previously generated lectures
    return jsonify({"message": "Feature not yet implemented"}), 501
