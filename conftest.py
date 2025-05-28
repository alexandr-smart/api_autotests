import pytest
from config import load_config

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Выбор окружения: dev | prod"
    )

@pytest.fixture(scope="session")
def api_config(request):
    """Фикстура, возвращающая конфиг для выбранного окружения."""
    env = request.config.getoption("--env")
    return load_config(env)

@pytest.fixture
def api_headers(api_config):
    headers = {}
    if api_config.get("api_key"):
        headers["api_key"] = api_config["api_key"]
    return headers