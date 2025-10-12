from selenium import webdriver
from selenium.webdriver import Keys # чтобы вводить текст с клавиатуры
from selenium.webdriver.common.by import By # чтобы находить элементы на странице через "dom"
import time
import random



# browser = webdriver.Chrome() # Инициализация браузера, из библиотеки webdriver находим Chrome
# browser.get("https://en.wikipedia.org/wiki/Document_Object_Model") # переходим на страницу
# browser.save_screenshot("dom.png") # делаем скриншот страницы
# time.sleep(5) # устанавливаем время ожидания на странице
# browser.get("https://ru.wikipedia.org/wiki/Selenium")
# browser.save_screenshot("Selenium.png")
# time.sleep(5)
# browser.refresh() # обновляем страницу
# browser.quit()

# browser = webdriver.Chrome()
# browser.get("https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%A1%D0%BF%D0%B5%D1%86%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D1%8B")
#
# assert "Википедия" in browser.title
#
# search_box = browser.find_element(By.ID, "searchInput")# Задаем поиск по ID, прописываем значение ID, можно поиск и по другим значениям,
# # например XPATH-это полный путь до конкретного элемента. Оба варианта удобны, так как уникальные значения.
# #этими действиями мы находим элемент на странице и сохраняем в переменную
#
# search_box.send_keys("Солнечная система") # вводим текст в поисковую строку .send_keys(). Но это пока только ввод, без получения информации
# search_box.send_keys(Keys.RETURN) # отправляем запрос
#
# a = browser.find_element(By.LINK_TEXT, "Солнечная система")
# a.click()
# time.sleep(5)

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

# paragraphs = browser.find_elements(By.TAG_NAME, "p")
#
# for paragraph in paragraphs:
#     print(paragraph.text)
#     input() # остается пустым, чтобы между параграфами нажимать Enter


hatnotes = []

for element in browser.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable ts-main":
        hatnotes.append(element)

print(hatnotes)
hatnote = random.choice(hatnotes)
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)
time.sleep(5)