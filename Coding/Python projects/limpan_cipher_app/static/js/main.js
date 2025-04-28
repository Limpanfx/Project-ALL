// main.js - Client-side functionality for the Limpan Cipher web interface

document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const englishText = document.getElementById('englishText');
    const limpanText = document.getElementById('limpanText');
    const encodedResult = document.getElementById('encodedResult');
    const decodedResult = document.getElementById('decodedResult');
    const encodeBtn = document.getElementById('encodeBtn');
    const decodeBtn = document.getElementById('decodeBtn');
    const copyEncodedBtn = document.getElementById('copyEncodedBtn');
    const copyDecodedBtn = document.getElementById('copyDecodedBtn');

    // Event listeners
    encodeBtn.addEventListener('click', encodeText);
    decodeBtn.addEventListener('click', decodeText);
    copyEncodedBtn.addEventListener('click', () => copyToClipboard(encodedResult));
    copyDecodedBtn.addEventListener('click', () => copyToClipboard(decodedResult));

    // Handle Enter key in textareas
    englishText.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && e.ctrlKey) {
            encodeText();
        }
    });

    limpanText.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && e.ctrlKey) {
            decodeText();
        }
    });

    // Function to encode text
    function encodeText() {
        const text = englishText.value.trim();
        if (!text) {
            showAlert('Please enter text to encode', 'warning');
            return;
        }

        // Call the API to encode
        fetch('/encode', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                showAlert(data.error, 'danger');
            } else {
                encodedResult.value = data.result;
                showAlert('Text encoded successfully!', 'success', 2000);
            }
        })
        .catch(error => {
            console.error('Error during encoding:', error);
            showAlert('Failed to encode text: ' + error.message, 'danger');
        });
    }

    // Function to decode text
    function decodeText() {
        const text = limpanText.value.trim();
        if (!text) {
            showAlert('Please enter text to decode', 'warning');
            return;
        }

        // Call the API to decode
        fetch('/decode', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                showAlert(data.error, 'danger');
            } else {
                decodedResult.value = data.result;
                showAlert('Text decoded successfully!', 'success', 2000);
            }
        })
        .catch(error => {
            console.error('Error during decoding:', error);
            showAlert('Failed to decode text: ' + error.message, 'danger');
        });
    }

    // Function to copy text to clipboard
    function copyToClipboard(element) {
        if (!element.value) {
            showAlert('Nothing to copy', 'warning');
            return;
        }
        
        element.select();
        document.execCommand('copy');
        
        // Deselect the text
        window.getSelection().removeAllRanges();
        
        showAlert('Copied to clipboard!', 'success', 1500);
    }

    // Function to show alerts
    function showAlert(message, type, duration = 3000) {
        // Create alert element
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-3`;
        alertDiv.style.zIndex = '1050';
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        
        // Add to the DOM
        document.body.appendChild(alertDiv);
        
        // Auto-dismiss after duration
        setTimeout(() => {
            alertDiv.classList.remove('show');
            setTimeout(() => {
                document.body.removeChild(alertDiv);
            }, 150);
        }, duration);
    }
});