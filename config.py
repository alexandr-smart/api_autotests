import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    if not base_url:
        raise ValueError("BASE_URL не задана!")
    return base_url