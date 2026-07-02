# 🤖 Offline Chatbot Using Ollama

An offline AI chatbot built with **Python**, **Streamlit**, and **Ollama**. This application provides a simple ChatGPT-like interface that runs locally on your computer, allowing you to interact with large language models without relying on cloud-based APIs.

## Features

* 💬 ChatGPT-style conversational interface
* 🧠 Local AI inference using Ollama
* 🔒 Fully offline after downloading the model
* ⚡ Fast responses with lightweight models
* 💾 Conversation history maintained during the session
* 🎨 Simple and intuitive Streamlit web interface

## Technologies Used

* Python
* Streamlit
* Ollama
* DeepSeek-R1 (1.5B) or Gemma 3 models

## Project Structure

```text
offline-chatbot/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── venv/               # Virtual environment (not included in Git)
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/offline-chatbot.git
cd offline-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

## Install Ollama

Download and install Ollama from:

https://ollama.com/download

After installation, download a language model:

```bash
ollama pull deepseek-r1:1.5b
```

or

```bash
ollama pull gemma3:latest
```

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## Example Questions

* Explain machine learning in simple terms.
* Write a Python program to reverse a string.
* Summarize this paragraph.
* Explain recursion with an example.
* Generate SQL queries for a student database.
* Help me debug this code.
* Write a professional email.

## Limitations

* Requires Ollama to be installed locally.
* Internet access is not available to the model by default.
* The chatbot only remembers messages within the current session.
* Smaller models may produce less accurate responses than larger models.

## Future Improvements

* Streaming responses
* Dark mode
* File upload (PDF, TXT)
* Chat history export
* Voice input and output
* Web search integration
* Retrieval-Augmented Generation (RAG)

## Author

**Rohit Saud**

Electronics, Communication and Information Engineering Student

## License

This project is released under the MIT License. Feel free to use, modify, and distribute it for educational and personal projects.
