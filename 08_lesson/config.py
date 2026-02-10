import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = "https://ru.yougile.com/api-v2"
    API_TOKEN = os.getenv("YOUGILE_API_TOKEN")
    
    @classmethod
    def get_headers(cls):
        return {
            "Authorization": f"Bearer {cls.API_TOKEN}",
            "Content-Type": "application/json"
        }
        