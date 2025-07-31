import requests
import json

# API base URL
BASE_URL = "http://localhost:5000"

def test_division_api():
    """Test the division API with various scenarios"""
    
    print("🧪 Testing Division API")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        {
            "name": "Basic division (10 / 2)",
            "data": {"numerator": 10, "denominator": 2},
            "expected_result": 5.0
        },
        {
            "name": "Decimal division (15.5 / 3)",
            "data": {"numerator": 15.5, "denominator": 3},
            "expected_result": 15.5 / 3
        },
        {
            "name": "Negative numbers (-20 / 4)",
            "data": {"numerator": -20, "denominator": 4},
            "expected_result": -5.0
        },
        {
            "name": "Zero numerator (0 / 5)",
            "data": {"numerator": 0, "denominator": 5},
            "expected_result": 0.0
        }
    ]
    
    # Test successful cases
    for test_case in test_cases:
        print(f"\n📝 Testing: {test_case['name']}")
        try:
            response = requests.post(
                f"{BASE_URL}/divide",
                json=test_case['data'],
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Success: {result['numerator']} / {result['denominator']} = {result['result']}")
                if abs(result['result'] - test_case['expected_result']) < 0.001:
                    print("   ✓ Result matches expected value")
                else:
                    print(f"   ⚠️  Expected: {test_case['expected_result']}, Got: {result['result']}")
            else:
                print(f"❌ Error: {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Connection Error: Make sure the server is running on http://localhost:5000")
            return
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
    
    # Test error cases
    print("\n" + "=" * 50)
    print("🚨 Testing Error Cases")
    print("=" * 50)
    
    error_cases = [
        {
            "name": "Division by zero",
            "data": {"numerator": 10, "denominator": 0}
        },
        {
            "name": "Missing denominator",
            "data": {"numerator": 10}
        },
        {
            "name": "Invalid input (string)",
            "data": {"numerator": "abc", "denominator": 2}
        },
        {
            "name": "Empty request body",
            "data": {}
        }
    ]
    
    for error_case in error_cases:
        print(f"\n📝 Testing: {error_case['name']}")
        try:
            response = requests.post(
                f"{BASE_URL}/divide",
                json=error_case['data'],
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code >= 400:
                result = response.json()
                print(f"✅ Expected error: {response.status_code} - {result.get('error', 'Unknown error')}")
            else:
                print(f"❌ Unexpected success: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Connection Error: Make sure the server is running")
            return
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")

def test_health_endpoint():
    """Test the health check endpoint"""
    print("\n" + "=" * 50)
    print("🏥 Testing Health Endpoint")
    print("=" * 50)
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Health check: {result['status']} - {result['message']}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the server is running")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

def test_home_endpoint():
    """Test the home endpoint"""
    print("\n" + "=" * 50)
    print("🏠 Testing Home Endpoint")
    print("=" * 50)
    
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Home endpoint: {result['message']}")
            print("Available endpoints:")
            for endpoint, description in result['endpoints'].items():
                print(f"   - {endpoint}: {description}")
        else:
            print(f"❌ Home endpoint failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the server is running")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    print("🚀 Division API Test Suite")
    print("Make sure the server is running with: python app.py")
    print("=" * 50)
    
    test_health_endpoint()
    test_home_endpoint()
    test_division_api()
    
    print("\n" + "=" * 50)
    print("✨ Test suite completed!")
    print("=" * 50) 