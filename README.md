# 🧠 AI Research Agent

An **AI-powered research assistant** built with [LangChain](https://www.langchain.com/), [Anthropic Claude](https://console.anthropic.com/), and [OpenAI](https://platform.openai.com/).  
It helps you research any topic by combining LLM reasoning with external tools (search, wiki lookup, saving sources), and outputs a **structured research summary**.

---

## ✨ Features
- 🔍 **Automated Research** – Ask any question, the agent fetches and summarizes relevant information.  
- 📚 **Tool-augmented** – Uses custom tools (`search_tool`, `wiki_tool`, `save_tool`) for better accuracy.  
- 📊 **Structured Output** – Returns results as a validated `Pydantic` model with:
  - Topic  
  - Summary  
  - Sources  
  - Tools used  
- ⚡ **LLM Flexibility** – Works with Anthropic’s Claude or OpenAI’s GPT models.  

---

## 🛠️ Tech Stack
- **Python 3.10+**  
- [LangChain](https://python.langchain.com/)  
- [Anthropic Claude API](https://docs.anthropic.com/) / [OpenAI API](https://platform.openai.com/)  
- [Pydantic](https://docs.pydantic.dev/) for structured outputs  
- Custom tools (`search_tool`, `wiki_tool`, `save_tool`)  

---
