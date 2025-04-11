#!/usr/bin/env python3

"""
Entry point for the Limpan Cipher web application.
This module imports the Flask app from app.py to be used by Gunicorn.
"""

from app import app  # noqa: F401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)