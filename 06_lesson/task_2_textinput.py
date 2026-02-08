from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("http://uitestingplayground.com/textinput")

    # Вводим текст в поле
    text_input = driver.find_element(By.ID, "newButtonName")
    text_input.send_keys("SkyPro")

    # Нажимаем на кнопку
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Ждем, пока текст кнопки изменится на SkyPro
    wait.until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

    # Получаем текст кнопки
    updated_button = driver.find_element(By.ID, "updatingButton")
    print(updated_button.text)

finally:
    driver.quit()
