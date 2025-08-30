# # Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# #
# # Требования:
# #
# # 1. Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# #
# # 2. Класс `Admin`: Этот класс должен наследоваться от класса `User`.
# # Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# # Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).
# #
# # 3. Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).
#
# user_list = []
#
# class User:
#     def __init__(self, user_id, name):
#         self._user_id = user_id
#         self._name = name
#         self._access_level = 'user'
#
#     def get_user_id(self):
#         return self._user_id
#
#     def get_name(self):
#         return self._name
#
#     def get_access_level(self):
#         return self._access_level
#
#
# class Admin(User):
#     def __init__(self, user_id, name, admin_password):
#         super().__init__(user_id, name)
#         self.access_level = 'admin'
#         self.admin_password = admin_password
#
#
#     def add_user(self, user, user_list):
#         user_list.append(user)
#
#     def remove_user(self, user_list, user):
#         user_list.remove(user)
#
# admin = Admin(1, 'admin', 'password')
# user1 = User(2, 'user1')
# user2 = User(3, 'user2')
#
# admin.add_user(user1, user_list)
# admin.add_user(user2, user_list)
# admin.remove_user(user_list, user1)
#
# print(user1.get_user_id())
# print(user1.get_name())
# print(user1.get_access_level())
# print(user2.get_user_id())
# print(user2.get_name())
# print(user2.get_access_level())


# Решение преподавателя

class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = 'admin'

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Пользователь добавлен в список")

    def remove_user(self, user_list, user):
        user_list.remove(user)
        print(f"Пользователь удален из списка")

users = []
admin = Admin("a1", 'Ivan')
user1 = User("u1", 'Petr')

print(user1.get_name())
admin.add_user(users, user1)

