from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse
from .gpt_client import stream_gpt_response

router = APIRouter()

@router.post("/api/advisor")
async def advisor(request: Request):
    data = await request.json()
    user_input = data.get("query")

    if not user_input:
        raise HTTPException(status_code=400, detail="Query is required")

    async def event_stream():
        async for chunk in stream_gpt_response(user_input):
            yield chunk

    return StreamingResponse(event_stream(), media_type="text/event-stream")