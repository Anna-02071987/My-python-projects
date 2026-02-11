# Lesson 8 - Yougile API tests (Projects)
Автотесты API для **Yougile** на **pytest + requests**.
Покрыты методы Projects:
- POST /api-v2/projects
- PUT /api-v2/projects/{id}
- GET /api-v2/projects/{id}

## Запуск
### 1) Установить зависимости
```bash
pip install pytest requests flake8
```

### 2) Задать переменные окружения (PowerShell)
Токен не хранится в коде — только в переменных окружения.
```powershell
$env:YOUGILE_BASE_URL="https://ru.yougile.com"
$env:YOUGILE_API_TOKEN="YOUR_TOKEN"
```

### 3) Запуск тестов
```bash
pytest 08_lesson -v
```

### 4) Проверка стиля
```bash
flake8 08_lesson
```

## Что сделано
- API-клиент вынесен в 08_lesson/client/yougile_api.py
- Тесты лежат в 08_lesson/tests/
- Позитивные тесты для POST/PUT/GET
- Негативные тесты для POST/PUT/GET
- Тесты стабильные: данные создаются автоматически (фикстура created_project)
- Секреты (токен) не коммитятся и не хранятся в репозитории

## Структура проекта
```
08_lesson/
+-- client/
¦   +-- __init__.py
¦   L-- yougile_api.py
+-- tests/
¦   +-- __init__.py
¦   +-- conftest.py
¦   L-- test_projects.py
+-- config.py
L-- README.md
```
