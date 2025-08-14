class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 8

    def eat(self):
        print(f"{self.name} ест")
        self.power += 2

    def hit(self):
        print(f"{self.name} ударяет")
        self.endurance -= 5

    def walk(self):
        print(f"{self.name} идет")

    def info(self):
        print(f"Имя воина: {self.name}")
        print(f"Сила воина: {self.power}")
        print(f"Выносливость воина: {self.endurance}")
        print(f"Цвет волос воина: {self.hair_color}")

war1 = Warrior("Стёпа", 76, 54, "черный")
war2 = Warrior("Андрюша", 10, 15, "брюнет")


war1.sleep()
war1.eat()
war1.hit()
war1.walk()
war1.info()

war2.sleep()
war2.eat()
war2.hit()
war2.walk()
war2.info()




