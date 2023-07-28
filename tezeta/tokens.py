from tiktoken import Tokenizer 

max_tokens = 2000

def count_text_tokens(text):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)
    return len(tokens)

def count_chat_tokens(chats):
    tokenizer = Tokenizer()
    tokens = sum([count_text_tokens(chat['content']) for chat in chats])
    return len(tokens)