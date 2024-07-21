"""
This module initializes the routes Blueprint for the Flask application.

It imports and registers the lecture and text-to-speech (tts) routes.

The Blueprint is named "routes" and can be used to organize
related views and other code.
"""

from flask import Blueprint

from . import lecture, tts

routes = Blueprint("routes", __name__)
