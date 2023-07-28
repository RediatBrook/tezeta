from . import tokens
import pinecone
import openai

"""

This function ensures that messages are in the following format.

messages = [
    {
        "role" : "user" or "assistant" or "system",
        "content" : "message content",
    },
    ...
    ]

"""

vector_db_type = "pinecone"
pinecone_api_key = ""
openai_api_key = ""
supported_vector_dbs = {"pinecone"}
pinecone_index_name = "tezeta"
pinecone_dimensions = 1536

def set_pinecone_dimensions(dimensions):
    pinecone_dimensions = dimensions

def set_pinecone_index_name(name):
    pinecone_index_name = name
    
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

def set_openai_key(key):
    openai_api_key = key
    
def validate_messages(messages):
    acceptable_roles = {"user", "assistant", "system"}

    if not isinstance(messages, list):
        raise ValueError("messages must be a list")

    for message in messages:
        if not isinstance(message, dict):
            raise ValueError("Each message must be a dictionary")

        if "role" not in message or "content" not in message:
            raise ValueError("Each message dictionary must have 'role' and 'content' keys")

        if message["role"] not in acceptable_roles:
            raise ValueError(f"Invalid role {message['role']}. Role must be one of {acceptable_roles}")
    return True


def rank_and_return_messages(messages, new_chat):
    
    # Initialize Pinecone
    pinecone.init(api_key=pinecone_api_key)

    # Create an index if it doesn't exist
    if pinecone_index_name not in pinecone.list_indexes():
        pinecone.create_index(pinecone_index_name, dimension=pinecone_dimensions)

    # Create a Pinecone Index instance
    index = pinecone.Index(pinecone_index_name)

    # Upsert vectors to Pinecone and keep a mapping from IDs to messages
    id_to_message = {}
    for i, msg in enumerate(messages):
        id_to_message[str(i)] = msg
        index.upsert(vectors=[(str(i), msg['content'])])

    # Query Pinecone for the top matches
    query_response = index.query(vector=new_chat, top_k=len(messages))

    # Filter results to fit within the max_context_window
    sorted_results = []
    total_tokens = 0
    for res in query_response.matches:
        original_message = id_to_message[res.id]
        tokens_in_result = tokens.count_chat_tokens(original_message)
        if total_tokens + tokens_in_result <= tokens.max_tokens:
            sorted_results.append(original_message)
            total_tokens += tokens_in_result
        else:
            break

    # Sort results based on their original order
    sorted_results = sorted(sorted_results, key=lambda x: messages.index(x))

    return sorted_results


def fit_messages(messages, new_chat):
    if validate_messages(messages):
        if(tokens.count_chat_tokens(messages) < tokens.max_tokens):
            return messages
        else:
            return rank_and_return_messages(messages, new_chat)
    return messages