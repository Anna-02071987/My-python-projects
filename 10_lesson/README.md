# Домашнее задание №10: Allure отчеты и PageObject

## 📋 Описание проекта
Автоматические тесты для двух веб-приложений с использованием:
- Selenium WebDriver
- PageObject паттерн
- Allure отчетность
- Pytest

## 🌐 Тестируемые сайты
1. **Калькулятор с задержкой**  
   https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
   
2. **Интернет-магазин**  
   https://www.saucedemo.com/

## 🧱 Структура проекта

## ✨ Реализовано
- ✅ PageObject паттерн для всех страниц
- ✅ Параметризация типов (type hints)
- ✅ Allure шаги и проверки
- ✅ Декораторы: `@allure.title`, `@allure.description`, `@allure.feature`, `@allure.severity`
- ✅ Проверка стиля flake8 (без ошибок)
- ✅ README.md с инструкциями

## 🚀 Запуск тестов

**1. Установка зависимостей**
```bash
pip install selenium pytest allure-pytest

Запуск всех тестов
pytest

Запуск с сохранением Allure результатов
pytest --alluredir=allure-results

Просмотр Allure отчета
allure serve allure-results

🛠 Технологии
Python 3.14

Selenium WebDriver

Pytest

Allure Framework

Git

📊 Пример Allure отчета
В отчете отображаются:

Подробные шаги каждого теста

Скриншоты (при необходимости)

Время выполнения

Статус проверок
