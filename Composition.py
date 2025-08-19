# Композиция
# Идея: "Целое ВЛАДЕЕТ частью" и отвечает за её жизненный цикл.
# Объект Engine создаётся ВНУТРИ Car, живёт столько же, сколько Car
# (если удалить Car — его Engine исчезнет вместе с ним).

class Engine():  # круглые скобки не обязательны в Python 3, но не являются ошибкой
    def start(self):
        print("Двигатель запущен")

    def stop(self):
        print("Двигатель остановлен")

class Car():
    def __init__(self):
        # композиция: Car СОЗДАЁТ свою "часть" (Engine) внутри себя
        # Car полностью контролирует жизненный цикл Engine
        self.engine = Engine()

    def start(self):
        # делегирование: Car вызывает метод своего компонента Engine
        self.engine.start()

    def stop(self):
        self.engine.stop()


my_car = Car()
my_car.start()  # используем поведение "части" через "целое" (Car -> Engine.start)
my_car.stop()


# Агрегация
# Идея: "Целое ССЫЛАЕТСЯ на часть", но НЕ владеет жизненным циклом.
# Объект Teacher создаётся СНАРУЖИ и передаётся в School.
# Teacher может существовать независимо от School и даже использоваться несколькими School.

class Teacher():
    def teach(self):
        print("Преподаватель учит")


class School():
    def __init__(self, new_teacher):
        # агрегация: School ПОЛУЧАЕТ уже созданный Teacher "снаружи"
        # School не отвечает за создание/удаление Teacher
        self.teacher = new_teacher

    def start_lesson(self):
        # делегирование поведения: School использует возможность Teacher
        self.teacher.teach()

my_teacher = Teacher()          # объект-часть создаётся вне "целого"
my_school = School(my_teacher)  # "целое" получает ссылку на часть
my_school.start_lesson()

# Подсказка для практики:
# Попробуй вызвать my_school.start_lesson() и затем удалить my_school:
# Teacher при этом останется жить (это и есть независимость при агрегации).
# my_school.start_lesson()
