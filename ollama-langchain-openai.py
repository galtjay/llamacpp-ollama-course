from openai import OpenAI
from langchain_ollama import ChatOllama

client = OpenAI(
    base_url='http://localhost:11434/v1/',

    # required but ignored
    api_key='ollama',
)

completion = client.chat.completions.create(model="deepseek-r1:1.5b",
                                            messages=[{
                                                "role": "user",
                                                "content": "你好,1+1等于多少?"
                                            }])
print(completion)
print("--------------------------------")
# https://python.langchain.com/docs/integrations/chat/ollama/
llm = ChatOllama(model="yylx:latest")

messages = [
    ("human", "你好,1+1等于多少?")
]

response = llm.invoke(messages)
print(response)
