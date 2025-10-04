# Задание 1: Получение данных
# 1. Импортируйте библиотеку `requests`.
# 2. Отправьте GET-запрос к открытому API (например, [https://api.github.com](https://api.github.com/)) с параметром для поиска репозиториев с кодом html.
# 3. Распечатайте статус-код ответа.
# 4. Распечатайте содержимое ответа в формате JSON.

# Задание 2: Параметры запрос
# 1. Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
# 2. Отправьте GET-запрос с параметром `userId`, равным `1`.
# 3. Распечатайте полученные записи.

# Задание 3: Отправка данных
# 1. Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
# 2. Создайте словарь с данными для отправки (например, `{'title': 'foo', 'body': 'bar', 'userId': 1}`).
# 3. Отправьте POST-запрос с этими данными.
# 4. Распечатайте статус-код и содержимое ответа.

# Задание 1
import  requests
import pprint

# params = {
#     "q": "html"
# }
#
# responce = requests.get("https://api.github.com/search/repositories", params=params)
# print(responce.status_code)
# pprint.pprint(responce.content)

# Задание 2
# url = "https://jsonplaceholder.typicode.com/posts"
#
# data = {
#     "userId": "1"
# }
#
# responce = requests.get(url, data=data)
# pprint.pprint(responce.content)

# Задание 3
url = "https://jsonplaceholder.typicode.com/posts"

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

responce = requests.post(url, data=data)
print(responce.status_code)
pprint.pprint(responce.content)