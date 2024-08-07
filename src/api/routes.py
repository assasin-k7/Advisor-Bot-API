from fastapi import APIRouter, Request, WebSocket
from .streaming import stream_gpt_response
from ..services.gpt_service import get_advice

router = APIRouter()

@router.post("/advice")
async def get_advice_endpoint(request: Request):
    data = await request.json()
    query = data.get("query", "")
    advice = await get_advice(query)
    return {"advice": advice}

@router.websocket("/ws/advice")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await stream_gpt_response(websocket)