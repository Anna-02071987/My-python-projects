# Домашнее задание №10

## Описание
Проект содержит автоматические тесты для:
- Калькулятора с задержкой (сайт: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)
- Интернет-магазина (сайт: https://www.saucedemo.com/)

Тесты написаны с использованием PageObject паттерна.

## Установка и запуск тестов

1. Установить зависимости:
   ```bash
   pip install selenium pytest allure-pytest

   Запустить все тесты:
 pytest

   Запустить тесты с сохранением результатов Allure:
pytest --alluredir=allure-results

   Просмотреть отчет Allure:
allure serve allure-results

Структура проекта
pages/ - классы PageObject для каждой страницы

tests/ - файлы с тестами

allure-results/ - папка с результатами тестов (создается после запуска)

Используемые технологии
Python

Selenium WebDriver

Pytest

Allure

