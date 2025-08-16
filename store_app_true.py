class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} добавлен в магазин {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удален из магазина {self.name}")
        else:
            print(f"Товар {item_name} не найден в магазине {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара {item_name} в магазине {self.name} обновлена")
        else:
            print(f"Товар {item_name} не найден в магазине {self.name}")

store1 = Store("Магазин 1", "ул. Пушкина, 1")
store2 = Store("Магазин 2", "ул. Толстого, 10")
store3 = Store("Магазин 3", "ул. Ленина, 5")

store1.add_item("хлеб", 50)
store1.add_item("молоко", 100)
store1.add_item("гречка", 60)

store1.remove_item("хлеб")

print(store1.get_price("молоко"))

store1.update_price("гречка", 80)

print(store1.get_price("гречка"))


