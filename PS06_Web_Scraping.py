#import requests
#from bs4 import BeautifulSoup
import time
import csv
from selenium import webdriver
#from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

# url = "https://quotes.toscrape.com/"
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, "html.parser")
#
# rows = soup.find_all("tr") # используется функция "find_all", тэг "tr" для поиска рядов в таблице
# data = []
#
# for row in rows:
#     cols = row.find_all("td") #td это колонки
#     cleaned_cols = [col.text.strip() for col in cols] #strip() убирает лишние пробелы; в скобках можно указать, что удалять
#     data.append(cleaned_cols)
#
# print(data)


# data = [
#     ['100', '200', '300'],
#     ['400', '500', '600']
#     ]

# numbers = []
#
# for row in data:
#     for text in row:
#         number = int(text)
#         numbers.append(number)
# print(numbers)


# list = []
#
# data = [
#     [100, 110, 120],
#     [400, 500, 600],
#     [150, 130, 140]
#     ]
#
# for row in data:
#     for item in row:
#         if item > 190:
#             list.append(item)
# print(list)

driver = webdriver.Chrome()
url  = "https://tomsk.hh.ru/vacancies/programmist"

driver.get(url)
time.sleep(5)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--n77Dj8TY8VIUF0yM')
print(f"[INFO] Найдено карточек вакансий: {len(vacancies)}")

parsed_data = []

for index, vacancy in enumerate(vacancies, start=1):
    try:
        print(f"\n[INFO] Обработка вакансии №{index}")

        try:
            title_element = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_6-0-13')
            title = title_element.text
            link = title_element.get_attribute('href')
        except NoSuchElementException:
            print("❌ Не найдено название вакансии")
            title = "Нет данных"
            link = "Нет ссылки"

        try:
            company = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_6-0-13').text
        except NoSuchElementException:
            print("⚠️ Не найдена компания")
            company = "Не указано"

        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, 'div.narrow-container--HaV4hduxPuElpx0V').text
        except NoSuchElementException:
            print("⚠️ Зарплата не найдена")
            salary = "Не указана"

        try:
            link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_6-0-13').get_attribute('href')
        except NoSuchElementException:
            print("⚠️ Ссылка не найдена")
            link = "Не указана"

        parsed_data.append([title, company, salary, link])
        print(f"✅ Успешно: {title} — {company} — {salary} - {link}")

    except Exception as e:
        print(f"🚨 Ошибка при парсинге вакансии №{index}: {e}")
        continue

with open('hh.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Компания', 'Зарплата', 'Ссылка'])
    writer.writerows(parsed_data)

print(f"\n[INFO] Готово! Сохранено {len(parsed_data)} записей в hh.csv")

driver.quit()




