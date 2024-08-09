import os

class Config:
    GPT_API_KEY = os.getenv("GPT_API_KEY", "your_default_api_key")
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
config =  Config()