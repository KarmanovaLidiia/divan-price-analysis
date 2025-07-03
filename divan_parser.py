from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv

# Настройки браузера
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
url = "https://www.divan.ru/category/divany"
driver.get(url)

# Подождём подольше
time.sleep(8)

# Попробуем более точный XPATH (на 2025 год)
prices = driver.find_elements(By.XPATH, "//span[@data-testid='price']")

print(f"🔎 Найдено {len(prices)} цен")

# Сохраняем в файл
with open("divan_prices.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Price"])
    for price in prices:
        text = price.text.strip()
        if text:  # фильтрация пустых
            writer.writerow([text])

driver.quit()
print("✅ Цены сохранены в файл 'divan_prices.csv'")
