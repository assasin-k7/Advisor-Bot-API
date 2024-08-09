import openai
from config import config

openai.api_key = config.GPT_API_KEY

async def stream_gpt_response(user_input: str):
    response = openai.Completion.create(
        engine="gpt-4",  # Example engine, adjust as needed
        prompt=user_input,
        max_tokens=150,
        stream=True
    )

    for chunk in response:
        if 'choices' in chunk:
            yield chunk['choices'][0]['text']