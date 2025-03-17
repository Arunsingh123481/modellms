from .openai_modellm import OpenAIModel
from .gemini_modellm import GeminiModel
from .stablediffusion_modellm import StableDiffusionModel
from .deepseek_modellm import DeepSeekModel
from PIL import Image

__version__ = "0.2.1"

def get_llm(model_type, api_key=None, repo_id=None):
    """
    Factory function to create an LLM interface.
    This matches the usage example in the README.
    
    Args:
        model_type (str): Type of model to use ("openai", "gemini", etc.)
        api_key (str, optional): API key for the model.
        repo_id (str, optional): Repository ID for certain models.
        
    Returns:
        LLMInterface: An instance of the LLMInterface class.
    """
    return LLMInterface(model_type, api_key, repo_id)

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