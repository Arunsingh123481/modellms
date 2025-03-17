from .openai_modellm import OpenAIModel
from .gemini_modellm import GeminiModel
from .stablediffusion_modellm import StableDiffusionModel
from .deepseek_modellm import DeepSeekModel
from PIL import Image
__version__ = "0.2.1"
class LLMInterface:
    def __init__(self, model_type, api_key=None, repo_id=None):
        model_type = model_type.lower().strip()
        
        if model_type == "openai":
            self.model = OpenAIModel(api_key)
            self.model_type = "text"
        elif model_type == "gemini":
            self.model = GeminiModel(api_key)
            self.model_type = "text"
        elif model_type == "deepseek":
            self.model = DeepSeekModel(api_key)
            self.model_type = "text"
        elif model_type in ["stable diffusion", "image"]:
            self.model = StableDiffusionModel(api_key, repo_id)
            self.model_type = "image"
        else:
            raise ValueError(f"Invalid model type: {model_type}")

    def query(self, prompt):
        try:
            response = self.model.query(prompt)
            if self.model_type == "image" and isinstance(response, Image.Image):
                return response
            return response
        except Exception as e:
            return f"Error: {str(e)}"