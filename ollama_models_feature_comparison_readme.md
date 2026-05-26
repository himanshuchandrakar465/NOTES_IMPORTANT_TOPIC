# Ollama Models Feature Comparison 🚀

A quick comparison table for popular models available in 【software】 Ollama.

---

## Feature Table

| Model | Chat | Tools / Function Calling | Streaming | Vision | Coding | Speed | Reasoning |
|---|---|---|---|---|---|---|---|
| Llama 3 | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Llama 3.1 | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Llama 3.2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mistral | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Qwen 2.5 | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅✅ |
| Qwen 2.5 Coder | ✅ | ✅ | ✅ | ❌ | ✅✅ | ✅ | ✅ |
| DeepSeek R1 | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅✅✅ |
| Phi-3 | ✅ | ✅ | ✅ | ❌ | ✅ | ✅✅ | ⚠️ |
| Gemma 2 | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| LLaVA | ✅ | ❌ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ |

---

## Feature Meaning

- ✅ = Supported / Good
- ❌ = Not Supported
- ⚠️ = Limited Support
- ✅✅ = Very Good
- ✅✅✅ = Excellent

---

# Best Models for Different Tasks

## 🔥 Best for LangChain Tool Calling

- Llama 3.1
- Qwen 2.5

---

## 💻 Best for Coding

- Qwen 2.5 Coder
- DeepSeek R1

---

## 🧠 Best for Reasoning

- DeepSeek R1

---

## ⚡ Best Lightweight / Fast Model

- Phi-3

---

## 👀 Best Vision Model

- Llama 3.2
- LLaVA

---

# Ollama Commands

## Install a Model

```bash
ollama pull llama3.1
```

## Run a Model

```bash
ollama run llama3.1
```

## List Installed Models

```bash
ollama list
```

## Remove a Model

```bash
ollama rm llama3
```

---

# Example LangChain Code

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1")

response = llm.invoke("Hello")

print(response.content)
```

---

# Tool Calling Example

```python
from langchain_ollama import ChatOllama
from langchain.tools import tool

model = ChatOllama(model="llama3.1")

@tool
def get_weather(location: str) -> str:
    """Get weather of a location"""

    return f"Sunny in {location}"

model_with_tools = model.bind_tools([get_weather])

response = model_with_tools.invoke(
    "What's the weather in Raipur?"
)

print(response)
```

---

# Recommended Beginner Setup 🚀

```bash
ollama pull llama3.1
pip install langchain langchain-ollama
```

Good balance of:

- Tool calling
- Speed
- Coding
- Reasoning
- LangChain support

