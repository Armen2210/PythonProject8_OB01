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
# class Report(): # обычный класс отчета.
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
# report.docPrinter() # выводит в консоль текст отчета


# Принцип подстановки Барбары Лисков - Liskov substitution principle(LSP)

# class Bird(): # Пример нарушения принципа. Обычный способ выполнения программы. В данном случае птица летит, но это пингвин, а он не умеет летать.
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):
#         print(f"{self.name} летит")
#
#
# class Penguin(Bird):
#     pass
#
# p = Penguin("Сильвестр")
# p.fly()



# class Bird(): # Пример реализации принципа подстановки Барбары Лисков. Создаем класс птицы, которая умеет летать.
#     def fly(self):
#         print("Эта птица летает")
#
# class Duck(Bird): # Создаем класс, который наследуется от класса птицы.
#     def fly(self):
#         print("Утка летает быстро")
#
# def fly_in_the_sky(animal): # Функция, которая принимает экземпляр класса птицы.
#     animal.fly()
#
# b = Bird()
# d = Duck()
#
# fly_in_the_sky(b)
# fly_in_the_sky(d)

 # В данном случае создан класс летающих птиц. Если нужно, создаем отдельный класс птиц: плавающих, бегающих,
# и создаем для них свои классы наследники. Так программа будет стабильно работать без внесения изменений.


# # Interface segregation principle(ISP) - принцип разделения интерфейса
#
# class SmartHouse(): # Обычная форма без принципа разделения интерфейса
#     def turn_on_light(self):
#         pass
#
#     def heat_food(self):
#         pass
#
#     def turn_on_music(self):
#         pass


# # Вариант с применением принципа разделения интерфейса
#
# class Light(): # Класс света
#     def turn_on(self):
#         print("Свет включен")
#
# class Food(): # Класс еды
#     def heat(self):
#         print("Еда разогревается")
#
# class Music(): # Класс музыки
#     def turn_on_music(self):
#         print("Музыка включена")
#
# # Созданы классы, которые реализуют свои интерфейсы.



# # Dependency inversion principle(DIP) - принцип инверсии зависимостей
#
# # Пример нарушения принципа. В данном случае класс StoryReader зависит от класса Book.
# class Book():
#     def read(self):
#         print("Читаем книгу")
#
# class StoryReader():
#     def __init__(self):
#         self.book = Book()
#
#     def tell_story(self):
#         self.book.read()


# # Вариант с применением принципа инверсии зависимостей
# from abc import ABC, abstractmethod
#
# class StorySource(ABC): # Абстрактный класс, с помощью которого можно создать в дальнейшем много источников
#     @abstractmethod
#     def get_story(self):
#         pass
#
# class Book(StorySource): # Источники, которые зависят от абстрактного класса
#     def get_story(self):
#         print("Чтение интересной истории")
#
# class AudioBook(StorySource): # Источники, которые зависят от абстрактного класса
#     def get_story(self):
#         print("Прослушивание интересной истории")
#
# class StoryReader(): # Класс, который использует эти источники и дает возможность выводить то, что есть в этих источниках
#     def __init__(self, story_source: StorySource):
#         self.story_source = story_source
#
#     def tell_story(self):
#         self.story_source.get_story()
#
#
# book = Book() # Создаем экземпляры классов
# audio_book = AudioBook() # Создаем экземпляры классов
#
# readerBook = StoryReader(book) # Передаем экземпляры классов в класс StoryReader
# readerBook.tell_story() # Выводим то, что есть в этих источниках
#
# readerAudioBook = StoryReader(audio_book) # Передаем экземпляры классов в класс StoryReader
# readerAudioBook.tell_story() # Выводим то, что есть в этих источниках