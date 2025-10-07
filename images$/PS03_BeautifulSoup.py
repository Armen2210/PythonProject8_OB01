import requests
from bs4 import BeautifulSoup
from googletrans import Translator


## Пример использования BeautifulSoup
# url = "http://quotes.toscrape.com/"
#
# response = requests.get(url)
# html = response.text
#
# soup = BeautifulSoup(html, "html.parser")
#
# links = soup.find_all("a") # используется функция "find_all", тэг "а" для поиска ссылок
#
# for link in links:
#     print(link.get("href"))



def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")


def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово?")
        if user == word:
            print("Правильно!")
        else:
            print(f"Неправильно! Правильный ответ - {word}")

        play_again = input("Хотите сыграть еще раз? (да/нет)")
        if play_again.lower() != "да":
            print("Спасибо за игру!")
            break

word_game()