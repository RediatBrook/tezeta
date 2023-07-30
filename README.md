# Tezeta: A Package for Maximizing Context Window Utilization in Chatbots (Under Development)

> :warning: **Tezeta is currently under active development and is not yet functional. The features listed below are planned for future releases.**

Tezeta is a Python package designed to optimize memory in chatbots and Language Model (LLM) requests using relevance-based vector embeddings. This tool aims to maximize the utilization of context windows, thereby improving chatbot performance by allowing the storage and retrieval of more relevant conversation history.

### Supported Features

- Using vector embeddings to rank chats based on relevance with OpenAI embeddings and Pinecone

## Planned Features

- Chunk up and rank sections of long text in a single chat or LLM request
- Using ChromaDB as vector store
- Support for using Open Source Embedding Models locally
- Support for using the Cohere API for Embeddings

## Installation

Installation instructions will be provided upon the first functional release of Tezeta.

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
import os

pinecone_api_key = os.environ.get("PINECONE_API_KEY")
open_ai_api_key = os.environ.get("OPENAI_API_KEY")

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
tezeta.set_pinecone_key(pinecone_api_key)
tezeta.set_openai_key(open_ai_api_key)
tezeta.set_max_tokens(30)
print(chats)
llm_chats = tezeta.chats.fit_messages(chats)
print (llm_chats)
```

## Documentation

Documentation will be available in the future.

## License

This project is licensed under the terms of the MIT license.