import os

class Config:
    GPT_API_KEY = os.getenv("GPT_API_KEY", "your_default_api_key")

config =  Config()