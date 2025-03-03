"""
This module provides functionality for text-to-speech conversion using Google Cloud Text-to-Speech API.

It includes functions to generate speech from text and list available voices.

Functions:
    generate_speech: Converts text to speech using specified language and voice.
    list_voices: Retrieves a list of available voices, optionally filtered by language code.

Dependencies:
    - google-cloud-texttospeech
    - app.config (for GOOGLE_APPLICATION_CREDENTIALS)

Note:
    Ensure that the GOOGLE_APPLICATION_CREDENTIALS environment variable is set
    with the path to your Google Cloud service account key file.
"""

import os

from google.cloud import texttospeech

from ..config import Config

conf = Config()

# Set Google Application Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = conf.GOOGLE_APPLICATION_CREDENTIALS

client = texttospeech.TextToSpeechClient()


def generate_speech(
    text: str, language_code: str = "en-US", voice_name: str = "en-US-Standard-C"
) -> bytes:
    """
    Generate speech from text using Google Cloud Text-to-Speech.

    Args:
        text (str): The text to convert to speech.
        language_code (str): The language code (e.g., 'en-US', 'es-ES').
        voice_name (str): The name of the voice to use.

    Returns:
        bytes: The audio content.
    """
    try:
        synthesis_input = texttospeech.SynthesisInput(text=text)

        voice = texttospeech.VoiceSelectionParams(
            language_code=language_code, name=voice_name
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        return response.audio_content
    except Exception as e:
        # Log the error here
        raise Exception(f"Failed to generate speech: {str(e)}")


def list_voices(language_code: str = None) -> list:
    """
    List available voices, optionally filtered by language code.

    Args:
        language_code (str, optional): The language code to filter voices.

    Returns:
        list: A list of available voices.
    """
    try:
        response = client.list_voices(language_code=language_code)
        return [
            {
                "name": voice.name,
                "language_codes": voice.language_codes,
                "ssml_gender": texttospeech.SsmlVoiceGender(voice.ssml_gender).name,
            }
            for voice in response.voices
        ]
    except Exception as e:
        # Log the error here
        raise Exception(f"Failed to list voices: {str(e)}")
