from venv import create

from langchain_openai import ChatOpenAI
from config import API_KEY,BASE_URL,MODEL

def create_llm(api_key=None):
    # 如果没有传入 Key，就使用本地 .env 中的 Key
            key = api_key or API_KEY
            if not key:
                   raise ValueError("请先配置 DeepSeek API Key")
            return ChatOpenAI(
                     model=MODEL,
                     api_key=key,
                     base_url=BASE_URL,
                     temperature=0.7
    )

def chat(messages, api_key=None):
    llm = create_llm(api_key)
    response = llm.invoke(messages)
    return response.content