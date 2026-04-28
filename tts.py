import os
from openai import OpenAI
from pathlib import Path

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

response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input="这是一段需要转换为语音的文字内容。"
)

# 保存为 MP3 文件
response.stream_to_file("output.mp3")
