# Free Cloud LLMs with Tool Calling

No download needed 🚀  
Use these models directly with APIs + LangChain.

---

# Install

```bash
uv add langchain python-dotenv
```

---

# Providers

| Provider | Models | Tool Calling | Free |
|---|---|---|---|
| Groq | Llama 3.3, DeepSeek, Qwen | ✅ | ✅ |
| OpenRouter | Many OSS models | ✅ | ✅ |
| Google AI Studio | Gemini | ✅ | ✅ |
| Together AI | Llama, Qwen | ✅ | Free credits |
| Cerebras | Llama | ✅ | ✅ |
| SambaNova | DeepSeek, Llama | ✅ | ✅ |
| Mistral AI | Mistral models | ✅ | ✅ |

---

# Recommended Models

## Groq

```python
model="llama-3.3-70b-versatile"
```

```python
model="deepseek-r1-distill-llama-70b"
```

---

## Google

```python
model="gemini-2.5-flash"
```

---

## OpenRouter

```python
model="qwen/qwen3-32b"
```

---

# API Keys

## Groq

`.env`

```env
GROQ_API_KEY=your_api_key_here
```

Get key: :contentReference[oaicite:0]{index=0}

---

## Google AI Studio

`.env`

```env
GOOGLE_API_KEY=your_api_key_here
```

Get key: :contentReference[oaicite:1]{index=1}

---

## OpenRouter

`.env`

```env
OPENROUTER_API_KEY=your_api_key_here
```

Get key: :contentReference[oaicite:2]{index=2}

---

# Example (Groq + LangChain)

## Install

```bash
uv add langchain langchain-groq python-dotenv
```

---

## Code

```python
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

response = llm.invoke("Explain AI")

print(response.content)
```

---

# Run

```bash
uv run main.py
```

---

# Git Ignore

```gitignore
.venv/
.env
__pycache__/
```

---

# Best Beginner Choice

1. Groq  
2. Google AI Studio  
3. OpenRouter