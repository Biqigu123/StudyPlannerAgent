import os

from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")

BASE_URL = os.getenv("BASE_URL"
                     ,"https://api.deepseek.com")
MODEL = "deepseek-chat"
