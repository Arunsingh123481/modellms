import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

class StableDiffusionModel:
    def __init__(self, api_key, model_id="stabilityai/stable-diffusion-2-1"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            use_auth_token=api_key
        ).to(self.device)
        
        if self.device == "cuda":
            self.pipe.enable_xformers_memory_efficient_attention()

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