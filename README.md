# 🤖 RAG Chatbot with Memory

A Retrieval-Augmented Generation (RAG) chatbot built using **LangChain**, **Google Gemini**, **FAISS**, and **Streamlit**. The chatbot answers questions from PDF documents while maintaining conversation memory.

## 🌐 Live Demo

🚀 Try the application here:

https://your-rag-chatbot.streamlit.app

> Note: This project uses the Google Gemini API for generating responses from PDF documents. The demo may be temporarily unavailable if the free Gemini API quota has been exhausted.


## 🚀 Features

* PDF document processing
* Semantic search using FAISS
* Conversation memory
* Google Gemini integration
* Fast document retrieval
* Streamlit web interface
  
## 🛠️ Technologies Used

| Technology    | Purpose                |
| ------------- | ---------------------- |
| Python        | Backend Logic          |
| Streamlit     | Web Application        |
| LangChain     | RAG Framework          |
| Google Gemini | AI Response Generation |
| FAISS         | Vector Database        |
| PDF Loader    | Document Processing    |
| Embeddings    | Semantic Search        |
| GitHub        | Version Control        |

## 📸 Screenshot

![RAG Chatbot Interface](./screenshot/rag1.png)

## ⚙️ Installation

```bash
git clone https://github.com/Nehanayar/Rag-chatbot-with-memory.git
cd Rag-chatbot-with-memory

pip install -r requirements.txt

streamlit run chatbot.py
```

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

## 📂 Project Structure

```text
Rag-chatbot-with-memory/
├── main.py
├── mybot.py
├── requirements.txt
├── sample.pdf
├── screenshot/
│   └── rag1.png
├── README.md
└── LICENSE
```

## 📜 License

MIT License

## 👩‍💻 Author

Neha Nayar
