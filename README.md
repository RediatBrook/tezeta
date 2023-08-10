# Tezeta: A Package for Maximizing Context Window Utilization in Chatbots

> :warning: **Tezeta is still currently under active development.**

Tezeta is a Python package designed to optimize memory in chatbots and Language Model (LLM) requests using relevance-based vector embeddings. This tool aims to maximize the utilization of context windows, thereby improving chatbot performance by allowing the storage and retrieval of more relevant conversation history.

### Supported Features

- Using vector embeddings to rank chats based on relevance with OpenAI embeddings and Pinecone
- Using ChromaDB as vector store with the default all-MiniLM-L6-v2 
- Using ChromaDB as vector store
- Support for using Open Source Embedding Models locally (currently through all-MiniLM-L6-v2 with chromaDB)

## Planned Features

- Chunk up and rank sections of long text in a single chat or LLM request
- Support for using the Cohere API for Embeddings

## Installation

```bash
pip install tezeta
```

## Basic Usage

First, to set the necessary environment variables in your system, you can use the following terminal commands.

**For macOS/Linux:**

```bash
export PINECONE_API_KEY=your_api_key
export OPENAI_API_KEY=your_api_key
export PINECONE_ENVIRONMENT=your_pinecone_environment
```

**For Windows:**

```cmd
set PINECONE_API_KEY=your_api_key
set OPENAI_API_KEY=your_api_key
set PINECONE_ENVIRONMENT=your_pinecone_environment
```

You can use the package as follows:
```python
import tezeta

chats = [
    {
        "role" : "user",
        "content" : "Wellness is an important part of wellbeing. How are you tackling that in your life"
    },
    {
        "role" : "user",
        "content" : "Hello there Jon, I'm a less relevant text that is trying really really hard to excluded from this test."
    },
    {
        "role" : "assistant",
        "content" : "I'm doing well, how are you?"
    }
]

tezeta.set_max_tokens(30)

print(chats)
llm_chats = tezeta.chats.fit_messages(chats)
print (llm_chats)
```

## Documentation

Further Documentation will be available in the future.

## License

This project is licensed under the terms of the MIT license.
