# Домашнее задание №9 — Pytest + SQLAlchemy

## Описание

В рамках домашнего задания реализованы и протестированы операции работы с сущностью Student с использованием pytest, SQLAlchemy и PostgreSQL.

Проект демонстрирует:
- работу с БД через ORM
- использование pytest-фикстур
- написание unit-тестов для CRUD-логики
- мягкое удаление (soft delete)
- проверку качества кода с помощью flake8

---

## Операционная среда

- OS: Windows
- Python: 3.14
- База данных: PostgreSQL / SQLite (для тестов)
- ORM: SQLAlchemy 2.0
- Тестовый фреймворк: pytest
- Линтер: flake8

---

## Структура проекта

09_lesson/
├── db/
│   └── models.py          # Модель Student с soft delete
├── conftest.py            # Фикстуры pytest
├── test_students.py       # Тесты create, update, soft delete
├── .gitignore             # Игнорируем __pycache__
└── README.md              # Описание проекта

---

## Реализованные тесты

### test_create_student
- создаёт студента
- проверяет, что запись появилась в БД
- проверяет, что deleted_at = None

### test_update_student_email
- создаёт студента
- обновляет email
- проверяет, что изменения сохранены

### test_soft_delete_student
- создаёт студента
- выполняет мягкое удаление
- проверяет, что поле deleted_at заполнено

---

## Установка и запуск

### Установка зависимостей
pip install pytest sqlalchemy psycopg2-binary flake8

### Настройка подключения к БД
set DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/student_db

### Запуск тестов
pytest 09_lesson -v

### Проверка кода линтером
flake8 09_lesson

---

## Результат

Все 3 теста успешно проходят.  
Код соответствует требованиям PEP8 (flake8).  
Структура проекта чистая, без служебных файлов.