import pytest
import os

def pytest_configure(config):
    """Конфигурация pytest"""
    # Проверяем наличие необходимых переменных окружения
    token = os.getenv("YOUGILE_API_TOKEN")
    if not token or token == "your_api_token_here":
        pytest.exit("Ошибка: Не установлен YOUGILE_API_TOKEN. "
                   "Создайте файл .env с вашим токеном.")
