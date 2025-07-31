# PyApiToDevide

A simple Python HTTP server that provides a REST API for dividing two numbers.

## Features

- **POST /divide** - Divide two numbers with comprehensive error handling
- **GET /health** - Health check endpoint
- **GET /** - API documentation and help
- Input validation and error handling
- JSON request/response format
- Logging for operations

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd PyApiToDevide
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Server

Run the Flask application:
```bash
python app.py
```

The server will start on `http://localhost:5000`

### API Endpoints

#### 1. POST /divide
Divides the first number (numerator) by the second number (denominator).

**Request:**
```json
{
    "numerator": 10,
    "denominator": 2
}
```

**Response:**
```json
{
    "result": 5.0,
    "numerator": 10.0,
    "denominator": 2.0
}
```

#### 2. GET /health
Health check endpoint to verify the server is running.

**Response:**
```json
{
    "status": "healthy",
    "message": "Division API is running"
}
```

#### 3. GET /
API documentation and help.

**Response:**
```json
{
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
}
```

### Error Handling

The API handles various error scenarios:

- **400 Bad Request**: Missing fields, invalid input types, division by zero
- **500 Internal Server Error**: Unexpected server errors

Example error response:
```json
{
    "error": "Division by zero",
    "message": "Denominator cannot be zero"
}
```

## Testing

Run the test suite to verify the API functionality:

```bash
python test_api.py
```

The test suite includes:
- Basic division operations
- Decimal number handling
- Negative number handling
- Error case testing (division by zero, invalid input, etc.)
- Health check verification

## Example Usage with curl

```bash
# Basic division
curl -X POST http://localhost:5000/divide \
  -H "Content-Type: application/json" \
  -d '{"numerator": 15, "denominator": 3}'

# Health check
curl http://localhost:5000/health

# Get API documentation
curl http://localhost:5000/
```

## Example Usage with Python requests

```python
import requests

# Divide two numbers
response = requests.post(
    'http://localhost:5000/divide',
    json={'numerator': 20, 'denominator': 4}
)

if response.status_code == 200:
    result = response.json()
    print(f"Result: {result['result']}")
else:
    print(f"Error: {response.json()}")
```

## Project Structure

```
PyApiToDevide/
├── app.py              # Main Flask application
├── test_api.py         # Test suite for the API
├── requirements.txt    # Python dependencies
└── README.md          # This documentation
```

## Requirements

- Python 3.6+
- Flask 3.0.0
- requests (for testing)

## License

This project is open source and available under the MIT License.
