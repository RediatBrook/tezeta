import tiktoken

max_tokens = 2000
encoder  = tiktoken.encoding_for_model("gpt-3.5-turbo-0613")

def count_text_tokens(text):
    tokens = encoder.encode(text)
    return len(tokens)

def count_chat_tokens(chats):
    if not chats:
        print("No chats to count.")
        return 0

    tokens = 0
    print("Counting chat tokens...")
    for chat in chats:
        tokens += count_text_tokens(chat['content'])
    print(f"Chat tokens: {tokens}")
    print("Done counting chat tokens.")
    return tokens

def set_max_tokens(new_max):
    max_tokens = new_max
