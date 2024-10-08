import json
import os
from dotenv import load_dotenv
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

# Load environment variables
load_dotenv()

def get_collection(path, collection_name):
    # Use OpenAI embedding function
    embedding_function = OpenAIEmbeddingFunction(
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name="text-embedding-ada-002"
    )
    
    client = chromadb.PersistentClient(path=path)
    collection = client.get_or_create_collection(collection_name, embedding_function=embedding_function)
    
    return collection

def initialize_collection(collection_name, source_json_file):
    collection = get_collection("./data/chroma", collection_name)
    
    if collection.count() == 0:
        with open(source_json_file) as json_file:
            source_json = json.load(json_file)
            
            ids = [str(item['id']) for item in source_json]
            documents = [item['document'] for item in source_json]
            metadatas = [item['metadata'] for item in source_json]
            
            collection.add(
                ids=ids,
                documents=documents,
                metadatas=metadatas
            )
    
    print(f"Initialized collection {collection_name}")
    
    return collection

if __name__ == "__main__":
    initialize_collection('company_info', 'data/company_info.json')