# # Пример привычного создания классов. Класс UserManager выполняет сразу несколько функций, которые связаны между собой.
# # Это не соответствует принципу SOLID.

# class UserManager: # Этот класс выполняет несколько функций, связанных между собой: создание пользователя, изменение имени пользователя, сохранение пользователя
#     def __init__(self, user):
#         self.user = user
#
#     def change_user_name(self, user_name):
#         self.user = user_name
#
#     def save_user(self):
#         file = open("user.txt", "a")
#         file.write(self.user)
#         file.close()

# # Пример реализации класса UserManager с применением принципа SOLID. Принцип единственной ответственности - Single Responsibility Principle(SRP).

# class User(): # Этот класс выполняет одну функцию - создание пользователя
#     def __init__(self, user):
#         self.user = user

# class UserNameChanger(): # Этот класс выполняет одну функцию - изменение имени пользователя
#     def __init__(self, user):
#         self.user = user

#     def change_name(self, new_name):
#         self.user = new_name

# class SaveUser(): # Этот класс выполняет одну функцию - сохранение пользователя
#     def __init__(self, user):
#         self.user = user

#     def save_user(self):
#         file = open("user.txt", "a")
#         file.write(self.user)
#         file.close()


# # Open/close principle(OCP) - принцип открытости/закрытости
#
#
# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def docPrinter(self):
#         print(f"Сформирован отчет: {self.title} - {self.content}")

# from abc import ABC, abstractmethod
#
# class Formated(ABC): # Абстрактный класс. Основа для других классов.
#     @abstractmethod
#     def format(self, report):
#         pass
#
#
# class TextFormated(Formated): # Класс-наследник
#     def format(self, report):
#         print(report.title)
#         print(report.content)
#
# class HtmlFormated(Formated): # Класс-наследник
#     def format(self, report):
#         print(f"<h1>{report.title}</h1>")
#         print(f"<p>{report.content}</p>")
#
# class Report(): # Класс, который использует абстрактный класс
#     def __init__(self, title, content, formated):
#         self.title = title
#         self.content = content
#         self.formated = formated
#
#     def docPrinter(self):
#         self.formated.format(self)
#
#
# report = Report("заголовок отчета", "текст отчета", TextFormated()) 
# #report = Report("заголовок отчета", "текст отчета", HtmlFormated())
#
# report.docPrinter()
