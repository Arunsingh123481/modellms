import requests

class DeepSeekModel:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("DeepSeek API key required")
        self.api_key = api_key
        self.endpoint = "https://api.deepseek.com/v1/chat/completions"

    def query(self, prompt):
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
            data = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7
            }
            response = requests.post(self.endpoint, headers=headers, json=data)
            return response.json()['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"DeepSeek Error: {str(e)}"