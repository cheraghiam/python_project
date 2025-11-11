<img src="./image/chatbot.png" alt="Rock Paper Scissors" width="400">

# Chatbot Dashboard using Ollama LLM & Streamlit

This project is a **local LLM-powered chatbot** built using **Ollama** as the language model backend and **Streamlit** as an interactive dashboard interface. The architecture is modular and organized into two main files: `app.py` and `utils.py`. It allows interactive chatting with a large language model in a clean, user-friendly dashboard.

## Features
- Local large-language-model inference using **Ollama**
- Interactive **Streamlit** dashboard for chatting
- Conversation history stored in session state
- Clean modular structure separating UI and backend logic
- Fully offline operation once models are downloaded
- Easily extendable and customizable for new features

## Project Structure
project/
├── app.py # Streamlit UI and main dashboard logic
├── utils.py # Backend helpers and Ollama request functions
└── README.md # Project documentation

bash
Copy code

## Requirements

**1. Install Ollama**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```
**2. Install Sreamlit and reaqusts**
```python 
pip install streamlit 
pip install requests
```
### Command-Line

Run the main script to see example conversions:
```bash
export PYTHON=`pwd`
python src/main.py
```

## Run project
- Command-Line
```bash
streamlit run app.py
```

## Project Structure

```
Chatbot
├── src/
│   ├── app.py   
│   ├── utils.py        
├── README.md   
|__imgae/
    |     
```
