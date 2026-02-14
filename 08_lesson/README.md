# Lesson 8 - Yougile API tests (Projects)

Автотесты API для Yougile на pytest + requests.
Покрыты методы Projects:
- POST /api-v2/projects
- PUT /api-v2/projects/{id}
- GET /api-v2/projects/{id}

## Запуск

### 1) Установить зависимости
pip install pytest requests flake8

### 2) Задать переменные окружения

**Для Windows PowerShell:**
$env:YOUGILE_BASE_URL="https://ru.yougile.com"
$env:YOUGILE_API_TOKEN="YOUR_TOKEN"

**Для Windows CMD:**
set YOUGILE_BASE_URL=https://ru.yougile.com
set YOUGILE_API_TOKEN=YOUR_TOKEN

**Для Linux/Mac:**
export YOUGILE_BASE_URL="https://ru.yougile.com"
export YOUGILE_API_TOKEN="YOUR_TOKEN"

### 3) Запуск тестов
pytest 08_lesson -v

### 4) Проверка стиля кода
flake8 08_lesson

## Что сделано

- API-клиент вынесен в 08_lesson/client/yougile_api.py
- Тесты лежат в 08_lesson/tests/
- Позитивные тесты для POST/PUT/GET
- Негативные тесты для POST/PUT/GET
- Тесты стабильные: данные создаются автоматически (фикстура created_project)
- Секреты (токен) не коммитятся и не хранятся в репозитории

## Структура проекта
08_lesson/
├── client/
│ ├── init.py
│ └── yougile_api.py
├── tests/
│ ├── init.py
│ ├── conftest.py
│ └── test_projects.py
├── .env.example
├── .gitignore
├── config.py
├── README.md
└── requirements.txt

## Примечания

- Создайте файл .env из .env.example и укажите свой токен
- Все тесты независимы благодаря использованию UUID
- Для корректной работы нужен действительный API токен Yougile