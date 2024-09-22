import os
import itertools
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv

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

def get_vector_search_results(collection, question):
    results = collection.query(
        query_texts=[question],
        n_results=4
    )
    
    return results

def get_similarity_search_results(question):
    collection = get_collection("./data/chroma", "company_info")
    
    search_results = get_vector_search_results(collection, question)
    
    flattened_results_list = list(itertools.chain(*search_results['documents'])) #flatten the list of lists returned by chromadb
    
    return flattened_results_list