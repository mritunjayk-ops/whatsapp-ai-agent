from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.models.schemas import (
    ChatRequest,
    ChatResponse
)

from app.routes.whatsapp import router as whatsapp_router

from app.services.ai_service import get_ai_response

from app.services.memory_service import clear_memory


app = FastAPI()


app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


app.include_router(whatsapp_router)


@app.get("/")
async def root():

    return {
        "message": "WhatsApp AI Agent is running"
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    response = await get_ai_response(request.message)

    return {
        "user_message": request.message,
        "ai_response": response
    }


@app.post("/reset-memory")
async def reset_memory():

    clear_memory()

    return {
        "message": "Conversation memory cleared successfully"
    }