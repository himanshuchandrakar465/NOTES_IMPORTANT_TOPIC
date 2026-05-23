# AI Models & Free Alternatives Guide

A practical guide for developers learning AI agents, LangChain, LangGraph, RAG, tool calling, coding assistants, and open-source LLMs.

---

# Best Paid AI Models

| Capability | Best Paid Models |
|---|---|
| General Chat | GPT-5, Claude Opus 4, Gemini 2.5 Pro |
| Coding | GPT-5 Codex, Claude Sonnet 4 |
| Tool Calling / Agents | GPT-5, Claude, Gemini |
| Reasoning / Math | OpenAI o3/o4, Gemini 2.5 Pro |
| Long Context | Gemini 2.5 Pro |
| Vision / Multimodal | GPT-5 Vision, Gemini Vision |
| Fast API | Groq Llama Models |
| Embeddings | text-embedding-3-large |
| Speech to Text | Whisper API |
| Image Generation | DALL·E |

---

# Best Free / Open Source Alternatives

| Capability | Free Alternative |
|---|---|
| General Chat | Llama 3.3 70B |
| Coding | DeepSeek Coder |
| Tool Calling | Qwen3, GLM-4 |
| Reasoning | DeepSeek R1 |
| Local Models | Ollama + Qwen / Llama |
| Vision | LLaVA, Qwen-VL |
| Embeddings | BGE-large, E5-large |
| Image Generation | Stable Diffusion XL |
| Speech to Text | Whisper Open Source |

---

# Best Hugging Face Models

## Tool Calling

```python
Qwen/Qwen3-32B
THUDM/GLM-4
Qwen/Qwen3-Coder
```

## Coding

```python
deepseek-ai/deepseek-coder
Qwen/Qwen3-Coder
codellama/CodeLlama-34b
```

## Chatbot

```python
meta-llama/Llama-3.3-70B-Instruct
google/gemma-3-27b-it
```

## Small Models (Laptop Friendly)

```python
microsoft/Phi-3-mini
google/gemma-2b
TinyLlama/TinyLlama-1.1B
```

---

# Best APIs for Beginners

| Provider | Good For |
|---|---|
| OpenAI | Best overall experience |
| Groq | Fast + free |
| Google Gemini | Large free quota |
| Hugging Face | Open-source models |
| Ollama | Run models locally |
| OpenRouter | Multiple models with one API |

---

# Recommended Stack for AI Engineers

## Beginner

- Python
- LangChain
- Ollama
- Llama 3
- ChromaDB
- FastAPI

## Intermediate

- LangGraph
- RAG
- Qwen3
- PostgreSQL
- Docker
- Redis

## Advanced

- Multi-Agent Systems
- MCP Servers
- Kubernetes
- Vector Databases
- Fine-Tuning
- Distributed Inference

---

# Best Free Setup for Learning

## Local AI Setup

Install Ollama:

```bash
ollama run llama3
```

Install packages:

```bash
uv add langchain langgraph langchain-openai langchain-community
```

---

# LangChain Agent Example

```python
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3")


def get_weather(city:str)->str:
    """Get weather for a city."""

    return f"Weather in {city} is sunny"


agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant"
)

response = agent.invoke({
    "messages":[
        {
            "role":"user",
            "content":"weather in delhi"
        }
    ]
})

print(response)
```

---

# Best Models by Use Case

| Use Case | Recommended Model |
|---|---|
| AI Agents | GPT-5 / Qwen3 |
| Coding Assistant | Claude Sonnet / DeepSeek Coder |
| Local Chatbot | Llama 3 |
| RAG | Qwen3 + BGE Embeddings |
| Small Laptop | Phi-3 Mini |
| Research | Gemini 2.5 Pro |
| Automation | Claude + MCP |

---

# Useful Links

## OpenAI
https://platform.openai.com

## Groq
https://console.groq.com

## Hugging Face
https://huggingface.co

## Ollama
https://ollama.com

## Google AI Studio
https://aistudio.google.com

## OpenRouter
https://openrouter.ai

---

# Suggested Learning Path

1. Python
2. APIs
3. LangChain
4. Prompt Engineering
5. RAG
6. Agents
7. LangGraph
8. Fine-Tuning
9. Deployment
10. Production AI Systems

---

# Notes

- OpenAI models are best for production.
- Groq is excellent for free fast inference.
- Ollama is best for local learning.
- Qwen and DeepSeek are strong free alternatives.
- LangGraph is becoming the standard for advanced AI agents.

