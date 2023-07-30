from . import tokens
from . import chats
from . import text
import os

vector_db_type = "pinecone"
pinecone_api_key = os.environ.get("PINECONE_API_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")
supported_vector_dbs = {"pinecone"}
pinecone_index_name = "tezeta-chats"
pinecone_environment = os.environ.get("PINECONE_ENVIRONMENT")
pinecone_dimensions = 1536

def set_pinecone_dimensions(dimensions):
    chats.pinecone_dimensions = dimensions

def set_pinecone_index_name(name):
    chats.pinecone_index_name = name
    
def set_vector_db(vector_db):
    if vector_db not in supported_vector_dbs:
        raise ValueError(f"Vector DB {vector_db} not supported. Supported vector DBs are {supported_vector_dbs}")
    chats.vector_db_type = vector_db
    
def get_vector_db():
    return vector_db_type

def set_pinecone_key(key):
    if vector_db_type != "pinecone":
        raise ValueError(f"Pinecone key can only be set when using pinecone as the vector DB")
    chats.pinecone_api_key = key

def set_openai_key(key):
    chats.openai_api_key = key
    
def set_max_tokens(new_max):
    tokens.max_tokens = new_max
    
    
    
    
    