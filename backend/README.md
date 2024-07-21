# Backend Main Module

## Overview

The `backend/main.py` file serves as the entry point for the Flask application. It is responsible for creating and running the Flask server.

## Key Components

- **Imports**: The module imports the `create_app` function from the `app` module.
- **Application Instance**: Creates an instance of the Flask application using the `create_app()` function.
- **Server Configuration**: 
  - Host: `0.0.0.0` (listens on all available network interfaces)
  - Port: `5555`

## Usage

When this script is run directly (not imported as a module), it starts the Flask development server with the specified host and port configurations.

## Running the Server

To start the server, execute the `backend/main.py` script:


python backend/main.py


This will start the Flask development server, making your application accessible at `http://localhost:5555` (assuming you're running it on your local machine).

## Note

The server is configured to run in development mode. For production deployment, consider using a production-grade WSGI server like Gunicorn or uWSGI.
