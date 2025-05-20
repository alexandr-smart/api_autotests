import allure
import pytest
# Импорт тестируемого клиента Petstore из модуля api.petstore_client
from api.petstore_client import PetstoreClient

# Фикстура с областью видимости на весь модуль (выполняется один раз для всех тестов)
@pytest.fixture(scope = "module")
def client():
    return PetstoreClient() # Создание и возвращение экземпляра PetstoreClient

@allure.feature("Pet API")
@allure.story("Получение питомца по ID")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка получения питомца по ID")
def test_get_pet_by_id(client):
    pet_id = 1
    with allure.step(f"Отправка запроса на получение питомца с ID {pet_id}"):
        response = client.get_pet_by_id(pet_id)

    with allure.step("Проверка кода ответа"):
        assert response.status_code in (200, 400), f"Получен код: {response.status_code}, ожидаемый 200 или 400"

    with allure.step("Вывод тела ответа"):
        allure.attach(str(response.text), name="Ответ", attachment_type=allure.attachment_type.TEXT)

    data = response.json()

    assert data ["id"] == 1, f"не равен одному"

def test_find_pets_by_status(client):
    response = client.find_pets_by_status("available")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_store_inventory(client):
    response = client.get_store_inventory()
    assert response.status_code == 200