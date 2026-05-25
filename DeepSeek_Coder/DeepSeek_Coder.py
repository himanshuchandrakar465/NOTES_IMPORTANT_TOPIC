from langchain_ollama import ChatOllama

llm = ChatOllama(model="deepseek-coder")

response = llm.invoke("Write snake game in python")

print(response.content)