from fastapi import WebSocket
from ..services.gpt_service import stream_gpt_advice

async def stream_gpt_response(websocket: WebSocket):
    while True:
        data = await websocket.receive_text()
        async for advice_chunk in stream_gpt_advice(data):
            await websocket.send_text(advice_chunk)