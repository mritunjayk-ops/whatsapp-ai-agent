from fastapi import APIRouter

from app.models.schemas import (
    ChatRequest,
    ChatResponse
)

from app.services.ai_service import get_ai_response


router = APIRouter()


@router.post("/webhook", response_model=ChatResponse)
async def webhook(request: ChatRequest):

    response = await get_ai_response(request.message)

    return {
        "user_message": request.message,
        "ai_response": response
    }