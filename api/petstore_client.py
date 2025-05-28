import allure
import requests
from env_loader import load_env
from conftest import api_headers

class PetstoreClient:
    def __init__(self):
        self.base_url = load_env()

    @allure.step("Отправка запроса на получение питомца")
    def get_pet_by_id(self, pet_id, headers = None):
        return requests.get(f"{self.base_url}/pet/{pet_id}", headers=headers)

    def find_pets_by_status(self, status):
        return requests.get(f"{self.base_url}/pet/findByStatus", params={"status": status})

    def get_store_inventory(self):
        return requests.get(f"{self.base_url}/store/inventory")