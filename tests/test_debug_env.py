def test_show_current_environment(api_config):
    """Просто выводит текущий BASE_URL в консоль."""
    print(f"\nТекущее окружение: BASE_URL = {api_config['base_url']}")  # Видно в pytest -v
    assert True  # Тест всегда проходит, но показывает хост