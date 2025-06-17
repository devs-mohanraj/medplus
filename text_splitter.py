from langchain.text_splitter import RecursiveCharacterTextSplitter
from load_data import docs
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(docs)