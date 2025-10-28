#import  matplotlib.pyplot as plt # pyplot - модуль для создания и оформления графиков
#import  numpy as np


# Линейная диаграмма
# x = [2, 6, 8, 14, 20]
# y = [6, 4, 10, 12, 16]
#
# plt.plot(x, y) # plot - функция для создания линейных графиков
#
# plt.title('Пример простого линейного графика') # title - функция для присвоения названия графику
# plt.xlabel('ось x')
# plt.ylabel('ось y')
#
# plt.show() # show - функция для вывода графика


# Гистограмма
# data = [5,6,6,6,6,7,5,8,7,9,7,10,11,8,6,8,11,9,7,8,6,8,12,8,7,8,9]
#
# plt.hist(data, bins=3) # hist - функция для создания гистограммы (как часто встречается значение), bins - указывает кол-во интервалов
# plt.xlabel('часы сна')
# plt.ylabel('кол-во людей')
# plt.title('гистограмма кол-ва часов сна')
# plt.show()


# Диаграмма рассеяния
# x = [1, 4, 6, 7]
# y = [3, 5, 8,10]
#
# plt.scatter(x, y) # scatter - функция для создания диаграммы рассеяния
#
#
# plt.xlabel('ось x')
# plt.ylabel('ось y')
# plt.title('тестовая диаграмма рассеяния')
# plt.show()

# a = np.array([1, 2, 3, 4]) # array - массив, в отличие от списка, хранит только однотипные данные
# print(a)
#
# a = np.zeros((3, 3)) # создаем массив из нулей размером 3*3
# print(a)
#
# a = np.ones((2, 5)) # создаем массив из единиц размером 2*5
# print(a)
#
# a = np.random.random((4, 5)) # создаем массив из случайных чисел размером 4*5
# print(a)
#
# a = np.arange(0, 10, 2) # создаем массив из чисел от 0 до 10 с шагом 2, последнее не выводится
# print(a)
#
# a = np.linspace(0, 1, 10) # создаем массив с равно распределенными числами между друг другом
# print(a)



# x = np.linspace(-10, 10, 100)
# y = x**2
#
# plt.plot(x, y)
# plt.xlabel('ось x')
# plt.ylabel('ось y')
# plt.title('График ф-ции y = x**2')
# plt.grid(True) # Эта функция выводит сетку(разметку) на графике
# plt.show()


# Создадим небольшой кейс с использованием построения графиков.#
# Есть сайт “циан”, на котором мы можем снимать или покупать квартиры. Нам нужно спарсить цены и составить график этих цен.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
import csv

driver = webdriver.Chrome()

url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
driver.get(url)

prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
   writer = csv.writer(file)
   writer.writerow(['Price'])  # Записываем заголовок столбца
   # Записываем цены в CSV файл
   for price in prices:
       writer.writerow([price.text])
# Закрытие драйвера
driver.quit()