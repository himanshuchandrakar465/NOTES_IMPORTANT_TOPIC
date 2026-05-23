# Llama 3.3 70B with LangChain

## Install

```bash
uv add langchain langchain-groq python-dotenv
```

---

## Create `.env`

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get API key from :contentReference[oaicite:0]{index=0}

---

## Run

```python
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

response = llm.invoke("What is LangChain?")

print(response.content)
```

---

## Start Project

```bash
uv run main.py
```