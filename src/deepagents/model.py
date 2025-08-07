from langchain_openai import ChatOpenAI


def get_default_model():
    return ChatOpenAI(model="gpt-4o", max_tokens=4096)
