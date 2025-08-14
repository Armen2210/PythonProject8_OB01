# *Дополнительное задание:
#
# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров.
# Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.

class Store:
    def __init__(self, store_name, address):
        self.store_name = store_name
        self.address = address
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_item_price(self, item):
        return self.items.get(item)

    def update_item_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price

store1 = Store("Магазин 1", "ул. Пушкина, 1")
store1.add_item("Телефон", 5000)
store1.add_item("Ноутбук", 8000)

store2 = Store("Магазин 2", "ул. Толстого, 10")
store2.add_item("Планшет", 6000)
store2.add_item("Компьютер", 12000)

store3 = Store("Магазин 3", "ул. Ленина, 5")
store3.add_item("Смартфон", 3000)
store3.add_item("Планшет", 7000)

store1.remove_item("Ноутбук")
store2.update_item_price("Планшет", 7500)
store3.add_item("Компьютер", 15000)

print(store1.items)
print(store2.items)
print(store3.items)