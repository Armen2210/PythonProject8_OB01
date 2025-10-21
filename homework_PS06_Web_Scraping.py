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
            title = sofa.find_element(By.CSS_SELECTOR, 'div.ProductCard_info__c9Z_4').text
        except NoSuchElementException:
            print("❌ Не найдено название позиции")
            title = "Нет данных"

        try:
            prices = sofa.find_elements(By.CSS_SELECTOR, "span[data-testid='price']")
            if len(prices) == 2:
                actualPrice = prices[0].text
                expiredPrice = prices[1].text
            elif len(prices) == 1:
                actualPrice = prices[0].text
                expiredPrice = "—"
            else:
                actualPrice = expiredPrice = "Не указано"
        except NoSuchElementException:
            actualPrice = expiredPrice = "Не указано"

        try:
            link = sofa.find_element(By.CSS_SELECTOR, 'a.url').get_attribute('href')
        except NoSuchElementException:
            print("⚠️ Ссылка не найдена")
            link = "Не указана"

        parsed_data.append([title, actualPrice, expiredPrice, link])
        print(f"✅ Успешно: {title} — {actualPrice} — {expiredPrice} - {link}")

    except Exception as e:
        print(f"🚨 Ошибка при парсинге карточки товара №{index}: {e}")
        continue

with open('hh.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название мебели', 'Цена со скидкой', 'Стандартная цена', 'Ссылка'])
    writer.writerows(parsed_data)

print(f"\n[INFO] Готово! Сохранено {len(parsed_data)} записей в hh.csv")

driver.quit()




