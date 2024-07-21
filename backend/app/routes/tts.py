"""
Text-to-Speech API routes.

This module contains Flask routes for text-to-speech functionality,
including generating speech from text and retrieving available voices.

Routes:
    /text_to_speech (POST): Converts text to speech and returns an audio file.
    /voices (GET): Returns a list of available text-to-speech voices.

Each route is protected by token authentication.
"""

import io

from app.services.text_to_speech import generate_speech
from app.utils.auth import token_required
from flask import jsonify, request, send_file

from . import routes


@routes.route("/text_to_speech", methods=["POST"])
@token_required
def text_to_speech():
    try:
        data = request.get_json()
        text = data.get("text")
        language = data.get("language", "en-US")
        voice = data.get("voice", "en-US-Standard-C")

        if not text:
            return jsonify({"error": "Missing text"}), 400

        audio_content = generate_speech(text, language, voice)

        # Convert audio content to a file-like object
        audio_file = io.BytesIO(audio_content)

        return send_file(
            audio_file,
            mimetype="audio/mp3",
            as_attachment=True,
            download_name="speech.mp3",
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@routes.route("/voices", methods=["GET"])
@token_required
def get_available_voices():
    # This is a placeholder for a potential future feature
    # to retrieve available TTS voices
    voices = [
        {"language": "en-US", "name": "en-US-Standard-C"},
        {"language": "en-US", "name": "en-US-Standard-D"},
        {"language": "en-GB", "name": "en-GB-Standard-A"},
        # Add more voices as needed
    ]
    return jsonify(voices), 200
