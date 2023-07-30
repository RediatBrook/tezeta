from . import tokens
import pinecone
import openai
import os


vector_db_type = "pinecone"
pinecone_api_key = os.environ.get("PINECONE_API_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")
supported_vector_dbs = {"pinecone"}
pinecone_index_name = "tezeta-chats"
pinecone_environment = os.environ.get("PINECONE_ENVIRONMENT")
pinecone_dimensions = 1536
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

    
def validate_messages(messages):
    acceptable_roles = {"user", "assistant", "system", "function"}

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


def get_embedding(message):
    content = message
    response = openai.Embedding.create(
        input = content,
        model = "text-embedding-ada-002"
    )
    embedding = response['data'][0]['embedding']
    return embedding
    
    

def rank_and_return_messages(messages, new_chat):
    
    # Initialize Pinecone
    pinecone.init(api_key=pinecone_api_key, environment=pinecone_environment)

    # Create a Pinecone Index instance
    index = pinecone.Index(pinecone_index_name)

    new_chat_length = tokens.count_text_tokens(new_chat['content'])

    # # Upsert vectors to Pinecone and keep a mapping from IDs to messages
    id_to_message = {}
    for i, msg in enumerate(messages):
        id_to_message[str(i)] = msg
        embedding = get_embedding(msg['content'])
        index.upsert(vectors=[{
            'id': str(i),
            'values' : embedding,
            'metadata':{'role': msg['role'], 'content': msg['content']},
        }])
        
    print(id_to_message)

    # # Query Pinecone for the top matches
    new_chat_embedding = get_embedding(new_chat['content'])
    query_response = index.query(vector=new_chat_embedding, top_k=len(messages))

    # Filter results to fit within the max_context_window
    sorted_results = []
    total_tokens = 0
    for res in query_response.matches:
        if(res.metadata==None):
            continue
        original_message = res.metadata['content']
        tokens_in_result = tokens.count_text_tokens(original_message['content'])
        if total_tokens + tokens_in_result + new_chat_length <= tokens.max_tokens:
            sorted_results.append(original_message)
            total_tokens += tokens_in_result
        else:
            break

    # Sort results based on their original order
    sorted_results = sorted(sorted_results, key=lambda x: messages.index(x))
    sorted_results.append(new_chat)

    return sorted_results


def fit_messages(messages):
    if validate_messages(messages):
        if(tokens.count_chat_tokens(messages) < tokens.max_tokens):
            return messages
        else:
            previous_messages = messages[:-1]
            new_message = messages[-1]
            return rank_and_return_messages(previous_messages, new_message)
    return messages