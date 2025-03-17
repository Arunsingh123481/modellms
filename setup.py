from setuptools import setup, find_packages
import os

if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description ="lUnified interface for multiple AI APIs",

setup(
    name="modellms",
    version="0.2.1",
    author="Arun Singh",
    author_email="arunsingh80475@gmail.com",
    description="Unified interface for multiple AI APIs including OpenAI, Gemini, Stable Diffusion, and DeepSeek",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/modellms",
    packages=find_packages(exclude=["tests*", "examples*"]),
    install_requires=[
        "openai>=1.0.0",
        "google-generativeai>=0.3.0",
        "diffusers>=0.20.0",
        "transformers>=4.30.0",
        "torch>=2.0.0",
        "accelerate>=0.20.0",
        "requests>=2.28.0",
        "Pillow>=10.0.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    keywords="ai ml openai gemini stable-diffusion deepseek",
    project_urls={
        "Documentation": "https://github.com/yourusername/modellms/wiki",
        "Source": "https://github.com/yourusername/modellms",
    },
)

