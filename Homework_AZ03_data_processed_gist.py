import pandas as pd
import matplotlib.pyplot as plt

file_path = 'cleaned_divan_prices.csv'
data = pd.read_csv(file_path)

# Берём два столбца
discounted_prices = data['Цена со скидкой']
standard_prices = data['Стандартная цена']

plt.figure(figsize=(8, 5))

# Гистограмма цен со скидкой
plt.hist(discounted_prices, bins=10, alpha=0.6, label='Цена со скидкой')

# Гистограмма стандартных цен
plt.hist(standard_prices, bins=10, alpha=0.6, label='Стандартная цена')

plt.title('Сравнение распределения цен')
plt.xlabel('Цена, ₽')
plt.ylabel('Частота')
plt.legend()
plt.show()
