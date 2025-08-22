# Задача №1 с использованием полиморфизма: Создайте класс Animal с методом make_sound(). Затем создайте несколько дочерних классов (например, Dog, Cat, Cow),
# которые наследуют Animal, но изменяют его поведение (метод make_sound()).
# В конце создайте список содержащий экземпляры этих животных и вызовите make_sound() для каждого животного в цикле.


# class Animal:
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         print("Гав-гав")
#
# class Cat(Animal):
#     def make_sound(self):
#         print("Мяу")
#
# class Cow(Animal):
#     def make_sound(self):
#         print("Мууу!")
#
#
# animals = [Dog(), Cat(), Cow()]
# for animal in animals:
#     animal.make_sound()


# Задача №2 с использованием полиморфизма: Продемонстрировать принцип полиморфизма через реализацию разных классов,
# представляющих геометрические формы, и метод для расчёта площади каждой формы.  Создать базовый класс Shape с методом area(),
# который просто возвращает 0. Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square),
# каждый из которых переопределяет метод area(). В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
# Написать функцию, которая принимает объект класса Shape и выводит его площадь.

# class Shape:
#     def area(self):
#         return 0
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
# def calculate_area(shape):
#     print("Площадь:", shape.area())
#
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
# square = Square(7)
#
# calculate_area(circle)
# calculate_area(rectangle)
# calculate_area(square)


#Задача №3. Создайте класс Author и класс Book. Класс Book должен использовать композицию для включения автора в качестве объекта.

# class Author:
#     def __init__(self, name, nationality):
#         self.name = name
#         self.nationality = nationality
#
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def get_info_book(self):
#         print(f"{self.title}, {self.author.name}, {self.author.nationality}")
#
# author = Author("F. Scott Fitzgerald", "American")
# book = Book("The Great Gatsby", author)
#
# book.get_info_book()
