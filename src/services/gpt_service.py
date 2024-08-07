import openai, os

from ..config import config
#Set your OpenAI API Key
openai.api_key = config.GPT_API_KEY

async def get_advice(query: str) -> str:
   response = openai.completions.create(
       engine = "text-davinci-003",
       prompt=query,
       max_tokens=150
   )
   return response.choices[0].text.strip()

async def stream_gpt_advice(query: str):
   # Currently, OpenAI API does not support real-time streaming.
   # This is a placeholder implementation. 
   response = openai.completions.create(
      engine="text-devinci-oo3",
      prompt=query,
      max_tokens=150
   )
   yield response.choices[0].text.strip()