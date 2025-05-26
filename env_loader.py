import os
from dotenv import load_dotenv

def load_env():
    environment = os.getenv("ENVIRONMENT", "dev").lower()
    dotenv_file = f".env.{environment}"
    if not os.path.exists(dotenv_file):
        raise FileNotFoundError(f"Файл {dotenv_file} не найден")
    load_dotenv(dotenv_file)
    print(f"[env_loader] Загружено окружение: {environment}, BASE_URL={os.getenv('BASE_URL')}")
