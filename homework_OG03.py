# Напишите функцию, которая высчитывает размер прибыли по заданной себестоимости и цены, по которой продают товар.

def calculate_profit(cost, price):
    profit = price - cost
    return profit

cost = float(input("Введите себестоимость товара: "))
price = float(input("Введите цену товара: "))

profit = calculate_profit(cost, price)
print(f"Размер прибыли составляет: {profit}")