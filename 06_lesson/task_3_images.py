from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    # Ждем, когда исчезнет индикатор загрузки
    wait.until(
        EC.invisibility_of_element_located((By.ID, "loading"))
    )

    # Находим все картинки
    images = driver.find_elements(By.TAG_NAME, "img")

    # Получаем src у третьей картинки (индекс 2)
    third_image_src = images[2].get_attribute("src")
    print(third_image_src)

finally:
    driver.quit()
