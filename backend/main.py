"""
This module serves as the entry point for the Flask application.

It imports the create_app function from the app module, creates the application
instance, and runs the server if the script is executed directly.

The server is configured to listen on all available network interfaces (0.0.0.0)
and port 5000.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555)
