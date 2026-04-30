import os
from openai import OpenAI

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    pass

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise SystemExit("未配置 OPENAI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.laozhang.ai/v1")
)

response = client.chat.completions.create(
    model="gpt-5.4",
    messages=[
        {"role": "user", "content": "介绍一下人工智能的发展历程"}
    ]
)

print(response.choices[0].message.content)
