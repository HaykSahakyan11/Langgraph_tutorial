from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

COLLECTION_NAME = "rag-chroma"
PERSIST_DIRECTORY = "./.chroma"

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

retriever = Chroma(
    collection_name=COLLECTION_NAME,
    persist_directory=PERSIST_DIRECTORY,
    embedding_function=OpenAIEmbeddings(),
).as_retriever()


def ingest() -> None:
    """Load the blog posts, split them into chunks, and store them in Chroma."""
    docs_list = WebBaseLoader(urls).load()

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250, chunk_overlap=0
    )
    doc_splits = text_splitter.split_documents(docs_list)

    Chroma.from_documents(
        documents=doc_splits,
        collection_name=COLLECTION_NAME,
        embedding=OpenAIEmbeddings(),
        persist_directory=PERSIST_DIRECTORY,
    )
    print(f"Stored {len(doc_splits)} chunks in {PERSIST_DIRECTORY}")


if __name__ == "__main__":
    # Run once before main.py to build the local vector store
    ingest()
