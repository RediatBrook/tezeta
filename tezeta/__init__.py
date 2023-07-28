from . import tokens
from . import chats
from . import text
from .text import fit_text as fit_text

vector_db_type = "chromadb"

supported_vector_dbs = {"pinecone", "chromadb"}

def set_vector_db(vector_db):
    if vector_db not in supported_vector_dbs:
        raise ValueError(f"Vector DB {vector_db} not supported. Supported vector DBs are {supported_vector_dbs}")
    vector_db_type = vector_db
    
def get_vector_db():
    return vector_db_type

def set_pinecone_key(key):
    if vector_db_type != "pinecone":
        raise ValueError(f"Pinecone key can only be set when using pinecone as the vector DB")
    pinecone_api_key = key
    
def set_max_tokens(tokens):
    if not isinstance(tokens, int):
        raise ValueError("max_tokens must be an integer")
    if tokens < 0:
        raise ValueError("max_tokens must be a positive integer")
    tokens.max_tokens = tokens
    
def get_max_tokens():
    return tokens.max_tokens
    

    
    