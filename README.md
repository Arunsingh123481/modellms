# ModelLMS

## Overview
A unified Python interface for interacting with leading AI models, including:
- 🤖 **Text Models**: OpenAI GPT, Google Gemini, DeepSeek
- 🎨 **Image Models**: Stable Diffusion
- 🔌 **Extensible Architecture**: Easily add new model integrations

## Key Benefits
- **Single Interface** - Interact with multiple AI providers through one API
- **Multimodal Support** - Handle both text generation and image creation
- **Production-Ready** - Error handling and memory-efficient operations
- **Flexible Deployment** - Works with both cloud APIs and local models

## Installation

### Local Development Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/modellms.git
   cd modellms

2. Create virtual environment (recommended):
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
3. Install dependencies:
   pip install -e .  # Editable mode for development

# Production Installation
pip install modellms

Configuration
Set API keys as environment variables:
# Text Models
export OPENAI_API_KEY="sk-your-key"
export GEMINI_API_KEY="AIzaSy..."
export DEEPSEEK_API_KEY="ds-your-key"

# Image Models (Stable Diffusion)
export HF_API_KEY="hf-your-key"

# Usage Examples
Basic Text Generation
from modellms import get_llm

# OpenAI Example
gpt = get_llm("openai", api_key="sk-...")
print(gpt.query("Explain quantum computing simply"))

# Gemini Example
gemini = get_llm("gemini", api_key="AIzaSy...")
print(gemini.query("Write a Python function to reverse a string"))

# Image Generation
# Stable Diffusion with custom model
sd = get_llm("stable diffusion", 
            api_key="hf-your-key",
            repo_id="stabilityai/stable-diffusion-2-1")

image = sd.query("Cyberpunk cat in neon-lit Tokyo")
image.save("output.png")

# CLI Interface
python main.py
# Follow prompts to select model and enter API keys
Key Features
Feature	Supported Models
Text Generation	- OpenAI, Gemini, DeepSeek
Image Generation - Stable Diffusion
Batch Processing - Coming Soon
Custom Model Hosting - Stable Diffusion (via HuggingFace)

# Troubleshooting
1. CUDA Errors: Ensure you have compatible NVIDIA drivers

2. Model Loading Issues:

For Stable Diffusion: Use official HuggingFace model IDs

Check disk space (>5GB required for diffusion models)

3. API Errors:

Verify API keys

Check provider status pages

# Contributing
1. Install development requirements:
pip install -r requirements_dev.txt

2. Run tests:
pytest tests/

3. Submit PRs following the contribution guidelines


# License

Key improvements:
1. **Clear Installation Paths** - Separate local dev vs production instructions
2. **Visual Feature Matrix** - Quick comparison of capabilities
3. **Troubleshooting Section** - Common issues and solutions
4. **Modern Formatting** - Tables and emojis for better readability
5. **Multi-Platform Support** - Includes Windows/Linux/Mac instructions
6. **Usage Variants** - Both Python API and CLI interface documented

To use this library effectively:
1. Start with text models (OpenAI/Gemini) for quick results
2. Use Stable Diffusion for creative projects (requires more RAM/VRAM)
3. Monitor API costs through provider dashboards
4. For local development, prefer Linux with NVIDIA GPU for best performance