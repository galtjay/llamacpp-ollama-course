import openai
from openai import OpenAI

API_BASE = "http://localhost:8080/v1/"
API_KEY = "any"  # 当使用本地服务器时，可以设置为任意非空字符串
client = OpenAI(api_key=API_KEY, base_url=API_BASE)

completion = client.chat.completions.create(model="DeepSeek-R1-Distill-Qwen",
                                            messages=[{
                                                "role":
                                                "user",
                                                "content":
                                                "Hi, who are you?"
                                            }])
print(completion)
