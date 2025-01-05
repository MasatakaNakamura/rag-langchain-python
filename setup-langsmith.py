import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

print(os.getenv("LANGCHAIN_TRACING_V2"))
print(os.getenv("LANGCHAIN_API_KEY"))
