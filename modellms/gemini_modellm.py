import google.generativeai as genai

class GeminiModel:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("Gemini API key required")
        
        genai.configure(api_key=api_key)
        
        # Try to use the newer model name, with fallback options
        try:
            # First try the current Gemini model
            self.model = genai.GenerativeModel('gemini-1.5-pro')
        except Exception as e:
            try:
                # Fall back to the older model name if necessary
                self.model = genai.GenerativeModel('gemini-pro')
            except Exception as e:
                raise ValueError(f"Could not initialize Gemini model: {str(e)}")
    
    def list_available_models(self):
        """List all available models for the given API key"""
        try:
            models = genai.list_models()
            return [model.name for model in models if "generateContent" in model.supported_generation_methods]
        except Exception as e:
            return f"Error listing models: {str(e)}"
    
    def query(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            # More descriptive error message
            error_msg = f"Gemini Error: {str(e)}"
            # Suggest using list_available_models if model not found
            if "not found" in str(e) or "not supported" in str(e):
                error_msg += "\nTry calling list_available_models() to see available models."
            return error_msg