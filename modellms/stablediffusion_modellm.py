import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

class StableDiffusionModel:
    def __init__(self, api_key=None, model_id="stabilityai/stable-diffusion-2-1"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Added handling for empty model_id
        if not model_id:
            model_id = "stabilityai/stable-diffusion-2-1"
            
        # Use auth token only if provided
        pipeline_args = {
            "pretrained_model_name_or_path": model_id,
            "torch_dtype": torch.float16 if self.device == "cuda" else torch.float32,
        }
        
        if api_key:
            pipeline_args["use_auth_token"] = api_key
            
        self.pipe = StableDiffusionPipeline.from_pretrained(**pipeline_args).to(self.device)
        
        # Enable memory efficient attention if available and using CUDA
        if self.device == "cuda":
            try:
                self.pipe.enable_xformers_memory_efficient_attention()
            except Exception:
                # Fallback if xformers is not available
                pass

    def query(self, prompt):
        try:
            image = self.pipe(
                prompt,
                num_inference_steps=25,
                guidance_scale=7.5,
                width=512,
                height=512
            ).images[0]
            return image
        except Exception as e:
            return f"Stable Diffusion Error: {str(e)}"