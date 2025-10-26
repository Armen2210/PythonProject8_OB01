import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data = {
#     "Набор А": [85, 90, 95, 100, 105],
#     "Набор Б": [70, 80, 95, 110, 120]
# }
#
# df = pd.DataFrame(data) # создание дата фрэйма
#
# stdA = df["Набор А"].std() # стандартное отклонение
# stdB = df["Набор Б"].std() # стандартное отклонение
#
# print(f'стандартное отклонение 1 набор - {stdA}')
# print(f'стандартное отклонение 2 набор - {stdB}')


# data = {
#     'Возраст': [23, 22, 21, 27, 23, 20, 29, 28, 22, 25],
#     'Зарплата': [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000]
# }
#
# df = pd.DataFrame(data)
#
# print(df.describe()) # выводится сразу вся информация, далее выведем отдельно
#
# print(f'Средний возраст - {df["Возраст"].mean()}')
# print(f'Медианный возраст - {df["Возраст"].median()}')
# print(f'Стандартное отклонение возраста - {df["Возраст"].std()}')
#
# print(f'Средняя зп - {df["Зарплата"].mean()}')
# print(f'Медианная зп - {df["Зарплата"].median()}')
# print(f'Стандартное отклонение зп - {df["Зарплата"].std()}')



# dates = pd.date_range(start='2022-07-26', periods=10, freq='D')
#
# values = np.random.rand(10) # создаем рандомно 10 значений
#
# df = pd.DataFrame({'Date': dates, 'Value': values}) # создаем словарь(дата фрэйм)
#
# df.set_index('Date', inplace=True) # устанавливаем колонку Date в качестве индекса всего дата фрэйма
# print(df)
#
# month = df.resample('M').mean() # делаем ресемплирование данных, считаем среднее значение для периода месяц('M')
# print(month)



# data = {'value': [1,2,2,3,3,3,4,4,4,4,5,6,7,8,9,10,55]}
# df = pd.DataFrame(data)
#
# # df['value'].hist() # для вывода диаграмм
# df.boxplot(column='value') # для вывода диаграмм
# plt.show() # показать диаграмму
#
# Q1 = df['value'].quantile(0.25) # Выводим значение первого квартиля - 25%
# Q3 = df['value'].quantile(0.75) # Выводим значение третьего квартиля - 25%
# IQR = Q3 - Q1 # вычисляем межквартальный размах
#
# downside = Q1 - 1.5 * IQR # нижняя граница
# upside = Q3 + 1.5 * IQR #верхняя граница
#
# df_new = df[(df['value'] >= downside) & (df['value'] <= upside)] # изменяем дата фрэйм так, чтобы все его значения были больше, чем нижнее значение (downside), и меньше, чем верхнее (upside)
# df_new.boxplot(column='value') # для вывода диаграмм
# plt.show() # показать диаграмму


data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data)

df['gender'] = df['gender'].astype('category') # преобразуем в категориальный тип командой .astype, теперь можно работать с категориями
df['department'] = df['department'].astype('category')

print(df['gender'].cat.categories) # выводим список категорий
print(df['department'].cat.categories)

print(df['department'].cat.codes) # выводим числовые коды категорий


df['department'] = df['department'].cat.add_categories(['Finance']) # добавляем новую категорию, обязательно нужно приравнять к первичному значению
print(df['department'].cat.categories)
df['department'] = df['department'].cat.remove_categories(['HR']) # удаляем новую категорию, обязательно нужно приравнять к первичному значению
print(df['department'].cat.categories)

print(df)