#!/usr/bin/env python3

"""
Web interface for the Limpan Cipher encoder/decoder.
This module provides a simple Flask web application to use the Limpan Cipher.
"""

import os
import logging
from flask import Flask, render_template, request, jsonify
from limpan_cipher import LimpanCipher

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "limpan_secret_key")

@app.route('/')
def index():
    """Render the main page of the application."""
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    """API endpoint to encode text."""
    try:
        data = request.get_json()
        text = data.get('text', '')
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        encoded_text = LimpanCipher.encode(text)
        return jsonify({'result': encoded_text})
    except Exception as e:
        logging.exception("Error in encode endpoint")
        return jsonify({'error': str(e)}), 500

@app.route('/decode', methods=['POST'])
def decode():
    """API endpoint to decode text."""
    try:
        data = request.get_json()
        text = data.get('text', '')
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        decoded_text = LimpanCipher.decode(text)
        return jsonify({'result': decoded_text})
    except Exception as e:
        logging.exception("Error in decode endpoint")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)