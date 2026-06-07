# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_community.vectorstores import FAISS
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
#
# embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/embedding-001",
#     google_api_key=os.getenv("GEMINI_API_KEY")
# )
#
# # load data from file
# loader = PyPDFLoader("sample.pdf")
# docs = loader.load()
#
# # split into chunks
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=200
# )
# chunks = splitter.split_documents(docs)
#
# # create vector db
# db = FAISS.from_documents(
#     documents=chunks,
#     embedding=embeddings
# )
#
# db.save_local("pdf_db")
# print("FAISS database created successfully!")



from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

# Embeddings

embeddings = HuggingFaceEmbeddings(
model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load PDF

loader = PyPDFLoader("sample.pdf")
docs = loader.load()

# Split PDF into chunks

splitter = RecursiveCharacterTextSplitter(
chunk_size=1000,
chunk_overlap=200
)

chunks = splitter.split_documents(docs)

# Create FAISS DB

db = FAISS.from_documents(
documents=chunks,
embedding=embeddings
)

# Save DB

db.save_local("pdf_db")

print("PDF database created successfully!")
