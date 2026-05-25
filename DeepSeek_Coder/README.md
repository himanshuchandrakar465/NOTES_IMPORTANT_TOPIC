# DeepSeek Coder with Ollama + LangChain 🚀

This project runs the DeepSeek Coder model locally using Ollama and LangChain.

---

# 1. Install Python Packages

```bash
pip install langchain langchain-ollama
```

---

# 2. Install Ollama

Download and install:

https://ollama.com/download/windows

After installation restart VS Code / Terminal.

Check installation:

```bash
ollama --version
```

---

# 3. Download DeepSeek Coder Model

```bash
ollama pull deepseek-coder
```

or directly run:

```bash
ollama run deepseek-coder
```

---

# 4. Start Ollama Server

Open terminal:

```bash
ollama serve
```

Keep this terminal running.

---

# 5. Python Code

Create `DeepSeek_Coder.py`

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="deepseek-coder")

response = llm.invoke("Write snake game in python")

print(response.content)
```

---

# 6. Run Project

```bash
python DeepSeek_Coder.py
```

---

# Common Errors

## Error:
```txt
WinError 10061
```

### Fix:
Start Ollama server:

```bash
ollama serve
```

---

## Error:
```txt
'ollama' is not recognized
```

### Fix:
Install Ollama and restart terminal.

---

# Useful Commands

## List Installed Models

```bash
ollama list
```

## Remove Model

```bash
ollama rm deepseek-coder
```

## Run Chat

```bash
ollama run deepseek-coder
```

---

# Recommended Models

| Model | Use Case |
|---|---|
| deepseek-coder | Coding |
| deepseek-r1 | Reasoning |
| llama3 | General AI |
| mistral | Fast lightweight |
| codellama | Code generation |

---

# Project Structure

```txt
project/
│
├── DeepSeek_Coder.py
├── README.md
└── venv/
```

---

# Official Links

- Ollama: https://ollama.com
- DeepSeek: https://www.deepseek.com
- LangChain: https://python.langchain.com