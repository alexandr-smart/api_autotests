import os

import allure
import requests
from dotenv import load_dotenv

load_dotenv()

class PetstoreClient:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")

    @allure.step("Отправка запроса на получение питомца")
    def get_pet_by_id(self, pet_id):
        return requests.get(f"{self.base_url}/pet/{pet_id}")

    def find_pets_by_status(self, status):
        return requests.get(f"{self.base_url}/pet/findByStatus", params={"status": status})


    def get_store_inventory(self):
        return requests.get(f"{self.base_url}/store/inventory")