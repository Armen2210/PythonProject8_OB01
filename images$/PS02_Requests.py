import requests
import pprint # позволяет красиво выводить словари

responce = requests.get("https://api.github.com/")
# print(responce.status_code) # выдает статус код
# print(responce.ok) # выдает True если статус код 200
#
# if responce.ok:
#     print("Запрос успешно выполнен")
# else:
#     print("Произошла ошибка")
#print(responce.text) # выдает HTML код страницы
#print(responce.content) # результатом запроса будет являться файл

responce_json = responce.json()
#print(responce_json)
pprint.pprint(responce_json)

