import requests

class DeepSeekModel:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("DeepSeek API key required")
        self.api_key = api_key
        self.api_url = "https://api.deepseek.com/v1/chat/completions"  # Replace with actual DeepSeek API endpoint
        
    def query(self, prompt):
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "deepseek-chat",  # Replace with actual model name
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }
            
            response = requests.post(self.api_url, headers=headers, json=payload)
            
            # Handle HTTP errors first
            if response.status_code != 200:
                return f"HTTP {response.status_code}: {response.text}"
                
            response_data = response.json()
            
            # Check for error messages
            if 'error' in response_data:
                return f"API Error: {response_data['error']['message']}"
                
            # Verify response structure
            if not all(key in response_data for key in ['choices', 'usage']):
                return f"Invalid response format: {response_data}"
                
            return response_data['choices'][0]['message']['content'].strip()
            
        except Exception as e:
            return f"Processing Error: {str(e)}"