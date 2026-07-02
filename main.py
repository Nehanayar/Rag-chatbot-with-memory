



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
