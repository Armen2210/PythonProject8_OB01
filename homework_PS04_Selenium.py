# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
# выйти из программы.

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title

userinput = input(f"Введите интересующую вас тему: ")

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(userinput)
search_box.send_keys(Keys.RETURN)
try:
    first_link = browser.find_element(By.CSS_SELECTOR, "ul.mw-search-results li a")
    browser.get(first_link.get_attribute("href"))
except:
    pass

choice = input(f"Пожалуйста, номер действия (1 или 2):\n"
      "1: Листать параграфы текущей статьи\n"
      "2: Перейти на одну из связанных страниц\n"
       "3: Выйти из программы\n"
        "Введите номер: ")

if choice == "1":
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input()

elif choice == "2":
    links = browser.find_elements(By.CSS_SELECTOR, "#bodyContent a")
    for i, link in enumerate(links[:10]):
        print(f"{i + 1}: {link.text}")
    num = int(input("Введите номер ссылки: ")) - 1
    browser.get(links[num].get_attribute("href"))

elif choice == "3":
    print("Выход из программы...")
    browser.quit()
    exit()


userchoice = input(f"Пожалуйста, выберите номер действия (1 или 2):\n"
      "1: Листать параграфы текущей статьи\n"
      "2: Перейти на одну из внутренних статей\n"
       "3: Выйти из программы\n"
        "Введите номер: ")

if userchoice == "1":
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input()

elif userchoice == "2":
    links = browser.find_elements(By.CSS_SELECTOR, "#bodyContent a")
    for i, link in enumerate(links[:20]):
        print(f"{i + 1}: {link.text}")
    num = int(input("Введите номер ссылки: ")) - 1
    browser.get(links[num].get_attribute("href"))

elif choice == "3":
    print("Выход из программы...")
    browser.quit()
    exit()

