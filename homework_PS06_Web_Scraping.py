import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException



driver = webdriver.Chrome()
url  = "https://www.divan.ru/sankt-peterburg/category/divany-i-kresla"

driver.get(url)
time.sleep(5)

sofas = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='product-card']")
print(f"[INFO] Найдено карточек товаров: {len(sofas)}")

parsed_data = []

for index, sofa in enumerate(sofas, start=1):
    try:
        print(f"\n[INFO] Обработка карточки товара №{index}")

        try:
            title = sofa.find_element(By.CSS_SELECTOR, "span[itemprop='name']").text.strip()
        except NoSuchElementException:
            print("❌ Не найдено название позиции")
            title = "Нет данных"


        try:
            actual_price = sofa.find_element(By.CSS_SELECTOR, "meta[itemprop='price']").get_attribute("content").strip()
        except NoSuchElementException:
            actual_price = "—"


        try:
            expired_price = sofa.find_element(By.XPATH, ".//*[contains(@class,'ExpiredPrice_expiredPrice')]").text.strip()
        except NoSuchElementException:
            expired_price = "—"


        try:
            link_el = sofa.find_element(By.XPATH, ".//a[starts-with(@href, '/product/')]")
            link = "https://www.divan.ru" + link_el.get_attribute("href")
        except NoSuchElementException:
            print("⚠️ Ссылка не найдена")
            link = "Не указана"

        parsed_data.append([title, actual_price, expired_price, link])
        print(f"✅ Успешно: {title} — {actual_price} — {expired_price} - {link}")

    except Exception as e:
        print(f"🚨 Ошибка при парсинге карточки товара №{index}: {e}")
        continue

with open('hh.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название мебели', 'Цена со скидкой', 'Стандартная цена', 'Ссылка'])
    writer.writerows(parsed_data)

print(f"\n[INFO] Готово! Сохранено {len(parsed_data)} записей в hh.csv")

driver.quit()




