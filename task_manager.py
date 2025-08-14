#Менеджер задач. Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False  # по умолчанию задача не выполнена

    def mark_as_done(self):
        self.completed = True

    def show_task(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        print(f"{self.description} (Срок: {self.deadline}) — {status}")



tasks = []


def add_task():
    print('Добавление задачи')
    description = input('Введите описание задачи: ')
    deadline = input('Введите срок выполнения задачи: ')
    tasks.append(Task(description, deadline))


def show_current_tasks():
    print("\nТекущие задачи:")
    for task in tasks:
        if not task.completed:
            task.show_task()

tasks.append(Task("пойти на пробежку", "вторник"))
tasks.append(Task("сходить в библиотеку", "четверг"))



show_current_tasks()
show_current_tasks()
add_task()
show_current_tasks()
tasks[2].mark_as_done()
show_current_tasks()