#import requests
#from bs4 import BeautifulSoup
import time
import csv
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

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

vacancies = driver.find_elemens(By.CLASS_NAME, 'vacancy-card--n77Dj8VIUF0yM')

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_6-0-13').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_6-0-13').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text_typography-label-1-regular___pi3R-_4-2-4"').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-button').get_attribute('href')
    except:
        print('Произошла ошибка при парсинге')
        continue

    parsed_data.append([title, company, salary, link])

with open('hh.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Компания', 'Зарплата', 'Ссылка'])
    writer.writerows(parsed_data)



driver.quit()
