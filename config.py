import os
from dotenv import load_dotenv

def load_config(env: str = "dev") -> dict:
    dotenv_file = f".env.{env}"
    if not os.path.exists(dotenv_file):
        raise FileNotFoundError(f"Missing .env file for {env}")

    load_dotenv(dotenv_file)

    return {
        "base_url": os.getenv("BASE_URL"),
        "env_name": env,
        # Всегда читаем API_KEY, если он есть в .env.{env}
        "api_key": os.getenv("API_KEY")
    }
