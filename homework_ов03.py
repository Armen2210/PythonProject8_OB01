#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#Дополнительно: Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.








class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

    def info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print("Chirp chirp")

    def eat(self):
        print("The bird is eating the worms")

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Color: {self.color}"

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("Roar roar")

    def eat(self):
        print("The mammal is eating the meat")

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Fur Color: {self.fur_color}"

class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        print("Hiss hiss")

    def eat(self):
        print("The reptile is eating the insects")

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Scale Color: {self.scale_color}"

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(f"Animals: {self.animals}\n")
            file.write(f"Employees: {self.employees}\n")

class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Feeding {animal.name}")

class Veterinarian:
    def heal_animal(self, animal):
        print(f"Healing {animal.name}")



def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

def animal_eat(animals):
    for animal in animals:
        animal.eat()



bird = Bird("Tweety", 2, "yellow")
mammal = Mammal("Lion", 5, "golden")
reptile = Reptile("Snake", 3, "green")

animals = [bird, mammal, reptile]
animal_sound(animals)
animal_eat(animals)
print(bird.info())
print(mammal.info())
print(reptile.info())

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_employee("John")
zoo.add_employee("Jane")

for animal in zoo.animals:
    print(animal.info())

for employee in zoo.employees:
    print(employee)

feed_animal = ZooKeeper()
feed_animal.feed_animal(bird)

heal_animal = Veterinarian()
heal_animal.heal_animal(mammal)

filename = "zoo.txt"
zoo.save_to_file(filename)



