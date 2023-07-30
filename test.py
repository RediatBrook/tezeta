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