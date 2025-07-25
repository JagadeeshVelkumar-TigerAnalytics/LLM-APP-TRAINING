import os
from dotenv import load_dotenv


load_dotenv()
base_url = "https://api.ai-gateway.tigeranalytics.com"
api_key = os.getenv("LLAMA_API_KEY")
open_ai_key = os.getenv("OPENAI_API_KEY")
text_embedding_api_key = os.getenv("TEXT_EMBEDDING_API_KEY")