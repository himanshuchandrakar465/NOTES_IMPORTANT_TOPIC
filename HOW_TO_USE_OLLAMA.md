# Ollama + DeepSeek Complete Guide 🚀

This guide explains:

- What is Ollama
- How to install Ollama
- How to run DeepSeek models
- Useful Ollama commands
- LangChain integration
- Common errors and fixes

---

# What is Ollama?

Ollama lets you run AI models locally on your computer.

You can run models like:

- DeepSeek
- Qwen
- Llama
- Mistral
- Gemma
- Phi

without API keys.

Official Website:

https://ollama.com

---

# Install Ollama (Windows)

## Step 1

Download Ollama:

https://ollama.com/download/windows

---

## Step 2

Install normally like any software.

---

## Step 3

Restart:

- VS Code
- PowerShell
- CMD

---

# Check Installation

Open terminal:

```bash
ollama --version
```

Example:

```txt
ollama version is 0.24.0
```

---

# Start Ollama

Usually Ollama starts automatically.

If needed:

```bash
ollama serve
```

---

# Fix "Port Already in Use"

If you see:

```txt
Only one usage of each socket address...
```

It means Ollama is already running ✅

You do NOT need `ollama serve`.

---

# Install DeepSeek Models

## DeepSeek R1

```bash
ollama pull deepseek-r1
```

---

## DeepSeek Coder

```bash
ollama pull deepseek-coder
```

---

# Run Models

## Run DeepSeek R1

```bash
ollama run deepseek-r1
```

---

## Run DeepSeek Coder

```bash
ollama run deepseek-coder
```

---

# Small Models (Better for Low RAM PCs)

## 1.5B Model

```bash
ollama pull deepseek-r1:1.5b
```

Run:

```bash
ollama run deepseek-r1:1.5b
```

---

# Useful Ollama Commands

## List Installed Models

```bash
ollama list
```

---

## Remove Model

```bash
ollama rm deepseek-r1
```

---

## Show Running Models

```bash
ollama ps
```

---

## Stop Running Model

```bash
ollama stop deepseek-r1
```

---

## Show Model Info

```bash
ollama show deepseek-r1
```

---

## Update Ollama

Download latest version again from:

https://ollama.com/download

---

# Install Python Packages

```bash
pip install langchain langchain-ollama
```

---

# Python Example

Create `main.py`

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1"
)

response = llm.invoke(
    "Explain reinforcement learning"
)

print(response.content)
```

---

# Run Python File

```bash
python main.py
```

---

# Change Models

## DeepSeek Coder

```python
llm = ChatOllama(model="deepseek-coder")
```

---

## Qwen3

```python
llm = ChatOllama(model="qwen3")
```

---

## GLM4

```python
llm = ChatOllama(model="glm4")
```

---

# Common Errors

## Error:
```txt
'ollama' is not recognized
```

### Fix:

Restart terminal or use:

```powershell
& "C:\Users\himan\AppData\Local\Programs\Ollama\ollama.exe" list
```

---

## Error:
```txt
model not found
```

### Fix:

Pull model first:

```bash
ollama pull deepseek-r1
```

---

## Error:
```txt
WinError 10061
```

### Fix:

Start Ollama:

```bash
ollama serve
```

---

# Recommended Models

| Model | Best For |
|---|---|
| deepseek-r1 | Reasoning |
| deepseek-coder | Coding |
| qwen3 | Best overall |
| mistral | Fast |
| llama3 | General AI |

---

# Project Structure

```txt
project/
│
├── main.py
├── README.md
└── venv/
```

---

# Official Links

- Ollama: https://ollama.com
- DeepSeek: https://www.deepseek.com
- LangChain: https://python.langchain.com