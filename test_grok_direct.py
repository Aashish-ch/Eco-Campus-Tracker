#!/usr/bin/env python
"""
Simple Grok API Test (standalone)
"""
import requests
import json

def test_grok_api_direct():
    """Test Grok API directly without Django"""
    api_key = "YOUR_API_KEY"
    base_url = "________"
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    print("🔑 Testing Grok API Key...")
    print(f"API Key: {api_key[:20]}...{api_key[-4:]}")
    print(f"Endpoint: {base_url}")
    
    # Test payload
    payload = {
        "model": "grok-beta",
        "messages": [
            {
                "role": "user",
                "content": "Hello, can you respond with just 'API Working'?"
            }
        ],
        "max_tokens": 50,
        "temperature": 0.7
    }
    
    try:
        print("\n🚀 Making API request...")
        response = requests.post(base_url, headers=headers, json=payload, timeout=15)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API Request Successful!")
            if 'choices' in result and result['choices']:
                content = result['choices'][0]['message']['content']
                print(f"AI Response: {content}")
            else:
                print(f"Unexpected response format: {result}")
        else:
            print(f"❌ API Request Failed: {response.status_code}")
            print(f"Error Response: {response.text}")
            
            # Try to parse error
            try:
                error_data = response.json()
                print(f"Error Details: {error_data}")
            except:
                print("Could not parse error response as JSON")
    
    except requests.exceptions.Timeout:
        print("❌ Request timed out")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def test_alternative_endpoints():
    """Test different possible endpoints"""
    api_key = "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"
    
    endpoints = [
        "https://api.x.ai/v1/chat/completions",
        "https://api.x.ai/v1/completions",
        "https://api.x.ai/chat/completions"
    ]
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    for endpoint in endpoints:
        print(f"\n🧪 Testing endpoint: {endpoint}")
        
        payload = {
            "model": "grok-beta",
            "messages": [{"role": "user", "content": "Test"}],
            "max_tokens": 20
        }
        
        try:
            response = requests.post(endpoint, headers=headers, json=payload, timeout=10)
            print(f"   Status: {response.status_code}")
            if response.status_code != 200:
                print(f"   Error: {response.text[:100]}...")
            else:
                print("   ✅ Success!")
                
        except Exception as e:
            print(f"   ❌ Failed: {e}")

if __name__ == "__main__":
    print("🤖 Grok API Direct Test")
    print("=" * 40)
    
    test_grok_api_direct()
    
    print("\n" + "=" * 40)
    test_alternative_endpoints()
