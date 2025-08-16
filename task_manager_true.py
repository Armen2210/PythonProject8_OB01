class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline,description):
        self.tasks.append({"deadline": deadline, "description": description, "status": "не выполнено"})

    def complete_task(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "Выполнено"
                print(f"Задача {description} выполнена")
            else:
                print(f"Задача {description} не найдена")

    def show_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if task["status"] == "не выполнено":
                print(f"{task['description']} — {task['deadline']}")

t = Task()
t.add_task("01.09.2025", "пойти на пробежку")
t.add_task("12.09.2025", "сходить в библиотеку")
t.add_task("10.09.2025", "пройти курс по Python")

t.show_tasks()
t.complete_task("сходить в библиотеку")
t.show_tasks()

