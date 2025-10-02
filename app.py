"""
License Plate Recognition Flask Application
"""
import os
import re
import requests
from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directory
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# API Configuration
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY', '458cf98460mshb89d2eea976a445p1d4e09jsne5bc3b367bac')
RAPIDAPI_HOST = os.getenv('RAPIDAPI_HOST', 'zyanyatech1-license-plate-recognition-v1.p.rapidapi.com')

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_url(url):
    """Validate if URL is properly formatted"""
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None

def recognize_license_plate(image_url):
    """
    Recognize license plate using external API
    
    Args:
        image_url (str): URL of the image to process
        
    Returns:
        tuple: (plate_number, confidence) or (None, None) if error
    """
    try:
        url = "https://zyanyatech1-license-plate-recognition-v1.p.rapidapi.com/recognize_url"
        
        querystring = {"image_url": image_url, "sourceType": "url"}
        
        payload = f'''{{
            "image_url": "{image_url}",
            "sourceType": "url"
        }}'''
        
        headers = {
            'x-rapidapi-key': RAPIDAPI_KEY,
            'x-rapidapi-host': RAPIDAPI_HOST,
            'Content-Type': 'application/json'
        }
        
        logger.info(f"Processing image URL: {image_url}")
        response = requests.post(url, data=payload, headers=headers, params=querystring, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if "results" in result and len(result["results"]) > 0:
                plate = result["results"][0]["plate"]
                confidence = result["results"][0]["confidence"]
                logger.info(f"Successfully recognized plate: {plate} with confidence: {confidence}")
                return plate, confidence
            else:
                logger.warning("No license plates detected in the image")
                return None, None
        else:
            logger.error(f"API request failed with status code: {response.status_code}")
            return None, None
            
    except requests.exceptions.Timeout:
        logger.error("API request timed out")
        return None, None
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
        return None, None
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return None, None

@app.route('/')
def home():
    """Home page"""
    return render_template('base.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Process license plate recognition request"""
    try:
        image_url = request.form.get('output', '').strip()
        
        if not image_url:
            flash('Please provide an image URL', 'error')
            return redirect(url_for('home'))
        
        if not validate_url(image_url):
            flash('Please provide a valid image URL', 'error')
            return redirect(url_for('home'))
        
        # Process the image
        plate, confidence = recognize_license_plate(image_url)
        
        if plate and confidence:
            result_message = f"License Plate: {plate} (Confidence: {confidence:.1f}%)"
            flash(result_message, 'success')
        else:
            flash('No license plate detected in the image. Please try with a different image.', 'warning')
        
        return redirect(url_for('home'))
        
    except Exception as e:
        logger.error(f"Error in predict function: {str(e)}")
        flash('An error occurred while processing the image. Please try again.', 'error')
        return redirect(url_for('home'))

@app.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'healthy', 'service': 'License Plate Recognition'}

@app.errorhandler(413)
def too_large(e):
    """Handle file too large error"""
    flash('File is too large. Maximum size is 16MB.', 'error')
    return redirect(url_for('home'))

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return render_template('base.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(e)}")
    flash('An internal error occurred. Please try again later.', 'error')
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Get configuration from environment
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    logger.info(f"Starting License Plate Recognition app on {host}:{port}")
    app.run(host=host, port=port, debug=debug)