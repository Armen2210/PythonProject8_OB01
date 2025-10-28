#1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.
# # Параметры нормального распределения
# mean = 0       # Среднее значение
# std_dev = 1    # Стандартное отклонение
# num_samples = 1000  # Количество образцов
#
# # Генерация случайных чисел, распределенных по нормальному распределению
# data = np.random.normal(mean, std_dev, num_samples)

import numpy as np
import  matplotlib.pyplot as plt

mean = 0
std_dev = 1
num_samples = 1000

data = np.random.normal(mean, std_dev, num_samples)
plt.hist(data, bins=10)
plt.xlabel('ось х')
plt.ylabel('ось у')
plt.title('Гистограмма для случайных данных')
plt.show()


# #2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`

import numpy as np
import  matplotlib.pyplot as plt

random_array1 = np.random.rand(5)
random_array2 = np.random.rand(5)

plt.scatter(random_array1, random_array2)

plt.xlabel('ось х')
plt.ylabel('ось у')
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.show()


#3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны
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
            title = sofa.find_element(By.CSS_SELECTOR, "div.ProductName").text.strip()
        except NoSuchElementException:
            print("❌ Не найдено название позиции")
            title = "Нет данных"


        try:
            actual_price = sofa.find_element(By.CSS_SELECTOR, "meta[itemprop='price']").get_attribute("content").strip()
        except NoSuchElementException:
            actual_price = "—"


        try:
            expired_price = sofa.find_element(By.XPATH, ".//*[contains(@class,'FullPrice_expired')]").text.strip()
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

with open('divan_prices.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название мебели', 'Цена со скидкой', 'Стандартная цена', 'Ссылка'])
    writer.writerows(parsed_data)

print(f"\n[INFO] Готово! Сохранено {len(parsed_data)} записей в hh.csv")

driver.quit()




