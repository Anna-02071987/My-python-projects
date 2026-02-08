from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("http://uitestingplayground.com/ajax")

    # Нажимаем на синюю кнопку
    ajax_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
    ajax_button.click()

    # Ждем появления зеленой плашки и получаем текст
    success_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    print(success_element.text)

finally:
    driver.quit()
