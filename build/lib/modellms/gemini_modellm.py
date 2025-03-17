import google.generativeai as genai

class GeminiModel:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("Gemini API key required")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def query(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Gemini Error: {str(e)}"