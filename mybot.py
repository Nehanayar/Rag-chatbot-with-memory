import streamlit as st
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0.3
)

# Hugging Face Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load PDF Database
pdf_db = FAISS.load_local(
    "pdf_db",
    embeddings,
    allow_dangerous_deserialization=True
)

# Load/Create Memory Database
if os.path.exists("memory_db"):
    memory_db = FAISS.load_local(
        "memory_db",
        embeddings,
        allow_dangerous_deserialization=True
    )
else:
    memory_db = FAISS.from_texts(
        ["memory initialized"],
        embeddings
    )

# Streamlit UI
st.title("📚 RAG Chatbot with Memory")

question = st.chat_input("Ask a question")

if "memories" not in st.session_state:
    st.session_state.memories = []

if question:

    # Search PDF
    pdf_docs = pdf_db.similarity_search(question, k=4)
    pdf_context = "\n".join(
        [doc.page_content for doc in pdf_docs]
    )

    # Search Memory
    memory_docs = memory_db.similarity_search(question, k=4)
    memory_context = "\n".join(
        [doc.page_content for doc in memory_docs]
    )

    prompt = f"""
You are a helpful assistant.

User Memories:
{memory_context}

PDF Context:
{pdf_context}

Current Question:
{question}

Instructions:
- Use PDF context first.
- Use memories if relevant.
- If the answer is not available in the PDF, clearly say so.
"""

    response = llm.invoke(prompt)
    answer = response.content

    # Store chat history
    st.session_state.memories.append(("user", question))
    st.session_state.memories.append(("assistant", answer))

    # Save memory
    docs = [
        Document(page_content=f"User: {question}"),
        Document(page_content=f"Assistant: {answer}")
    ]

    memory_db.add_documents(docs)
    memory_db.save_local("memory_db")

# Display chat history
for role, message in st.session_state.memories:
    with st.chat_message(role):
        st.write(message)