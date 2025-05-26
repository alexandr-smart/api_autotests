import allure
import requests
from config import load_env

class PetstoreClient:
    def __init__(self):
        self.base_url = load_env()

    @allure.step("Отправка запроса на получение питомца")
    def get_pet_by_id(self, pet_id):
        return requests.get(f"{self.base_url}/pet/{pet_id}")

    def find_pets_by_status(self, status):
        return requests.get(f"{self.base_url}/pet/findByStatus", params={"status": status})


    def get_store_inventory(self):
        return requests.get(f"{self.base_url}/store/inventory")