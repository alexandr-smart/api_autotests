import os
from dotenv import load_dotenv

def load_env():
    environment = os.getenv("ENVIRONMENT", "dev").lower()
    dotenv_file = f".env.{environment}"

    if os.path.exists(dotenv_file):
        load_dotenv(dotenv_file)
        print(f"[env_loader] Загружено окружение: {environment} из {dotenv_file}")
    else:
        load_dotenv()
        print(f"[env_loader] Файл {dotenv_file} не найден. Загружен fallback .env")

    base_url = os.getenv("BASE_URL")
    if not base_url:
        raise ValueError("BASE_URL не задана!")

    return base_url