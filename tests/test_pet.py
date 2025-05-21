import allure
import pytest
# Импорт тестируемого клиента Petstore из модуля api.petstore_client
from api.petstore_client import PetstoreClient
from utils.asserts import Asserts

# Фикстура с областью видимости на весь модуль (выполняется один раз для всех тестов)
@pytest.fixture(scope = "module")
def client():
    return PetstoreClient() # Создание и возвращение экземпляра PetstoreClient

@allure.feature("Pet API")
@allure.story("Получение питомца по ID")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка получения питомца по ID")
def test_get_pet_by_id(client):
    pet_id = 2
    response = client.get_pet_by_id(pet_id)

    asserts = Asserts(response)

    asserts.assert_status_code(200)
    asserts.assert_json_field_equals("id", 1)


def test_find_pets_by_status(client):
    response = client.find_pets_by_status("available")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_store_inventory(client):
    response = client.get_store_inventory()
    assert response.status_code == 200