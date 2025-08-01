from flask import Flask, request, jsonify
import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Configure logging to write to both console and file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/division_api.log'),
        logging.StreamHandler()  # This keeps console logging
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/divide', methods=['POST'])
def divide_numbers():
    """
    POST API endpoint that divides two numbers.
    
    Expected JSON payload:
    {
        "numerator": <first_number>,
        "denominator": <second_number>
    }
    
    Returns:
    {
        "result": <division_result>,
        "numerator": <first_number>,
        "denominator": <second_number>
    }
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            logger.warning("No JSON data provided in request")
            return jsonify({
                "error": "No JSON data provided",
                "message": "Please provide numerator and denominator in JSON format"
            }), 400
        
        # Extract numerator and denominator
        numerator = data.get('numerator')
        denominator = data.get('denominator')
        
        # Validate input
        if numerator is None or denominator is None:
            logger.warning(f"Missing required fields in request: numerator={numerator}, denominator={denominator}")
            return jsonify({
                "error": "Missing required fields",
                "message": "Both 'numerator' and 'denominator' are required"
            }), 400
        
        # Check if inputs are numbers
        try:
            numerator = float(numerator)
            denominator = float(denominator)
        except (ValueError, TypeError) as e:
            logger.warning(f"Invalid input type: numerator={numerator} (type: {type(numerator)}), denominator={denominator} (type: {type(denominator)})")
            return jsonify({
                "error": "Invalid input type",
                "message": "Both numerator and denominator must be numbers"
            }), 400
        
        
        # Perform division
        if denominator == 0:
    raise ValueError('Division by zero is not allowed')
result = numerator / denominator
        
        # Log the operation
        logger.info(f"Division operation: {numerator} / {denominator} = {result}")
        
        # Return result
        return jsonify({
            "result": result,
            "numerator": numerator,
            "denominator": denominator
        }), 200
        
    except Exception as e:
        import traceback
        error_traceback = traceback.format_exc()
        logger.error(f"Unexpected error: {str(e)}")
        logger.error(f"Stack trace:\n{error_traceback}")
        return jsonify({
            "error": "Internal server error",
            "message": "An unexpected error occurred"
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "Division API is running"
    }), 200

@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API documentation"""
    return jsonify({
        "message": "Division API Server",
        "endpoints": {
            "POST /divide": "Divide two numbers",
            "GET /health": "Health check",
            "GET /": "This help message"
        },
        "usage": {
            "POST /divide": {
                "description": "Divide numerator by denominator",
                "request_body": {
                    "numerator": "number (required)",
                    "denominator": "number (required)"
                },
                "example": {
                    "numerator": 10,
                    "denominator": 2
                }
            }
        }
    }), 200

if __name__ == '__main__':
    logger.info("Starting Division API Server...")
    app.run(host='0.0.0.0', port=5000, debug=True) 