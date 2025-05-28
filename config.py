import os
from pathlib import Path
from dotenv import load_dotenv


def load_config(env: str = "dev") -> dict:
    """Загружает конфиг из .env-файла по имени окружения."""
    env_file = Path(f".env.{env}")
    if not env_file.exists():
        raise FileNotFoundError(f"Env file {env_file} not found!")

    load_dotenv(env_file)  # Загружаем переменные в os.environ

    return {
        "base_url": os.getenv("BASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "timeout": int(os.getenv("TIMEOUT", 10)),
    }
