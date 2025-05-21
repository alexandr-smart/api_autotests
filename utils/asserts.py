import json
import allure

class Asserts:

    def __init__(self, response):
        self.response = response

    def _get_json(self):
        """Внутренний метод — пытается распарсить JSON и прикрепляет ответ, если не получается."""
        try:
            return self.response.json()
        except json.JSONDecodeError:
            self.attach_response()
            raise AssertionError("Ответ не является валидным JSON")

    def attach_response(self):
        """Аттачит тело ответа в Allure (текст и JSON, если возможно)."""
        try:
            json_data = self.response.json()
            allure.attach(
                json.dumps(json_data, indent=2, ensure_ascii=False),
                name="Ответ (JSON)",
                attachment_type=allure.attachment_type.JSON
            )
        except json.JSONDecodeError:
            # Если не JSON, прикрепим как текст
            allure.attach(
                self.response.text,
                name="Ответ (текст)",
                attachment_type=allure.attachment_type.TEXT
            )

    def assert_status_code(self, expected_status_code):
        """Универсальная проверка статус кода"""
        with allure.step(f"Проверка что что статус код равен - {expected_status_code}"):
            actual = self.response.status_code
            if actual != expected_status_code:
                self.attach_response()
            assert actual == expected_status_code, f"Ожидался статус {expected_status_code}, но получен {actual}"

    def assert_json_field_equals(self, field, expected_value):
        """Проверка определенного поля в ответе"""
        with allure.step(f"Проверка что поле {field} равно {expected_value}"):
            data = self._get_json()
            actual_value = data.get(field)
            if actual_value != expected_value:
                self.attach_response()
            assert actual_value == expected_value, f"Значение поля {field} == {actual_value}, но ожидалось {expected_value}"

    def assert_json_has_fields(self, *fields):
        """Проверка, что JSON содержит определенные поля"""
        with allure.step(f"Проверка, что JSON содержит поле {fields}"):
            data = self._get_json()
            for field in fields:
                assert field in data, f"Поле '{field}' отсутствует в ответе"

    def assert_json_structure(self, expected_structure: dict):
        """
                Проверка, что структура и типы данных в JSON соответствуют ожидаемым.

                Пример:
                    expected_structure = {
                        "id": int,
                        "name": str,
                        "status": str
                    }
                """
        with allure.step("Проверка структуры и типов полей JSON"):
            data = self._get_json()
            for field, expected_type in expected_structure.items():
                assert field in data, f"Поле '{field}, отсутствует в ответе'"
                actual_value = data[field]
                assert isinstance(actual_value, expected_type), (
                    f"Поле '{field}' имеет тип {type(actual_value).__name__}, "
                    f"ожидался {expected_type.__name__}"
                )



