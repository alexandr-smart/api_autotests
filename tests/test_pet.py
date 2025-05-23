import allure
import pytest
# Импорт тестируемого клиента Petstore из модуля api.petstore_client
from api.petstore_client import PetstoreClient
from utils.asserts import Asserts

# Фикстура с областью видимости на весь модуль (выполняется один раз для всех тестов)
@pytest.fixture(scope = "module")
def client():
    return PetstoreClient() # Создание и возвращение экземпляра PetstoreClient

@allure.sub_suite("Petstore API Tests")
@allure.feature("Pet API")
class TestPetApi:

    @allure.title("Проверка получения питомца по ID")
    def test_get_pet_by_id(self, client):
        pet_id = 2
        response = client.get_pet_by_id(pet_id)

        asserts = Asserts(response)

        asserts.assert_status_code(200)
        asserts.assert_json_field_equals("id", 2)


    @allure.title("Проверка получения питомца по статусу")
    @pytest.mark.parametrize("status", [
        "available",
        "pending",
        "sold",
        "available,pending",
        "available,sold",
        "pending,sold",
        "available,pending,sold"
    ])
    def test_find_pets_by_status(self, client, status):
        response = client.find_pets_by_status(status=status)
        print(f"Запрос по статусу '{status}': {response.request.url}")
        asserts = Asserts(response)

        asserts.assert_status_code(200)
        asserts.attach_response()


    def test_get_store_inventory(self, client):
        response = client.get_store_inventory()
        assert response.status_code == 200