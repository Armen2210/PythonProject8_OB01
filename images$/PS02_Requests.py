import requests
import pprint # позволяет красиво выводить словари


## в этой части учились работать с запросами
#responce = requests.get("https://api.github.com/")
# print(responce.status_code) # выдает статус код
# print(responce.ok) # выдает True если статус код 200
#
# if responce.ok:
#     print("Запрос успешно выполнен")
# else:
#     print("Произошла ошибка")
#print(responce.headers)
#print(responce.text) # выдает HTML код страницы
#print(responce.content) # результатом запроса будет являться файл


#responce_json = responce.json()
#print(responce_json)
#pprint.pprint(responce_json)

## в этой части делали запрос по заданным параметрам
# params = {
#     "q": "python" # q это query, он обозначает поисковый запрос, то есть, что будем искать
# }

# responce = requests.get("https://api.github.com/search/repositories", params=params) # ищем в репозиториях; params - задаем параметры, второе params - название переменной.
# Иначе говоря, при запросе к данной странице у нас будут указываться следующие параметры. В данном случае ищет python
#pprint.pprint(responce.json())
#print(f"Количество найденных репозиториев: {responce.json()['total_count']}")

## в этой части скачаем изображение
# img = "https://www.midowatches.com/media/catalog/product/cache/e90539398676e18af87c09c5bab406ae/M/0/M038.431.11.061.00_6_wrist_2.png?im=Resize=(1680,1680),aspect=fill;Crop=(0,0,1680,1680),gravity=Center"
#
# responce = requests.get(img) # Отправляем запрос на определенную страницу. Адрес прописываем в переменной "img" и подставляем сюда переменную. Можно подставить ссылку
#
# with open("test.jpg", "wb") as file: # open - открывает, а если нет, создаёт файл, w - записать в него инфу, которая сохранилась в responce, b - бинарное.
#     file.write(responce.content) # записать информацию, которая сохранилась в responce

# в этой часте отправляем post запросы

url = "https://jsonplaceholder.typicode.com/posts" # бесплатный онлайн сервис для тестирования

data = {
    "title": "тестовый post запрос",
    "body": "тестовый контент post запрос",
    "userId": 2
}

responce = requests.post(url, data=data) # первая data - это параметр, а вторая data - информация, которая в параметр передается
print(responce.status_code)
print(f"Ответ - {responce.json()}")