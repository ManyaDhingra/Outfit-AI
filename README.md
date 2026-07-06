# Outfit AI 👗

Outfit AI is a Streamlit application that classifies outfit images using OpenAI CLIP and provides outfit suggestions using Llama 3 via Ollama.

## Features

- Upload outfit images
- Outfit classification
- Chat with AI
- Outfit recommendations

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/Outfit-AI.git
cd Outfit-AI
pip install -r requirements.txt
```

Start Ollama

```bash
ollama serve
```

Download model

```bash
ollama pull llama3
```

Run

```bash
streamlit run app.py
```