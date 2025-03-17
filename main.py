import modellms
from PIL import Image

def main():
    print("AI Assistant - Choose Model:")
    print("1. OpenAI\n2. Gemini\n3. Stable Diffusion\n4. DeepSeek")
    
    choice = input("Select model (1-4): ")
    api_key = input("Enter API key: ").strip()
    
    model_map = {
        "1": "openai",
        "2": "gemini",
        "3": "stable diffusion",
        "4": "deepseek"
    }
    
    # Add repo_id input for Stable Diffusion
    repo_id = None
    if choice == "3":
        repo_id = input("Enter model repository ID (default: stabilityai/stable-diffusion-2-1): ").strip()
        if not repo_id:
            repo_id = "stabilityai/stable-diffusion-2-1"
    
    try:
        # Use the get_llm function instead of directly instantiating LLMInterface
        llm = modellms.get_llm(model_map[choice], api_key, repo_id)
        
        while True:
            prompt = input("\nEnter prompt (exit to quit): ")
            if prompt.lower() == "exit":
                break
            
            response = llm.query(prompt)
            
            if isinstance(response, Image.Image):
                response.save("output.png")
                print("Image saved as output.png")
            else:
                print(f"\nResponse: {response}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()