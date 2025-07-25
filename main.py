from fastapi import FastAPI
from fastapi import Request
from backend.llm_chat_bot import generate_chatbot_response_without_rag
from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501","http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class ChatInput(BaseModel):
#     user_input: str

@app.post("/chat")
async def chat(request: Request):
    print("reponse endpoint started")
    input_payload = await request.json()
    input = input_payload.get("user_input")
    response = generate_chatbot_response_without_rag(
        input
    )
    return {"response":response}

if __name__ == '__main__':
    app.run()