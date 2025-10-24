import pandas as pd

# data = {
#     'Name': ['John', 'Anna', 'Peter', 'Linda'],
#     'Age': [28, 22, 34, 42],
#     'City': ['New York', 'Paris', 'London', 'Berlin']
# }
#
# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv("csv_files/World-happiness-report-2024.csv")
# print(df.head(2)) # выводит первые строки дата фрэйма(по умолчанию 5)
# print(df.tail(3)) # выводит последние строки дата фрэйма
# print(df.info()) # выводит информацию о дата фрэйме
# print(df.describe()) # выводит основные статистические данные
# print(df['Country name']) # выводит данные по выбранному столбцу, первые и последние пять
# print(df[['Country name', 'Regional indicator']]) # выводит данные по выбранным столбцам, для этого двойные скобки
# print(df.loc[56]) # выводит все данные по выбранной строке
# print(df.loc[56, 'Social support']) # выводит выбранные данные по указанной строке
# print(df[df['Social support'] > 1.400]) # выводит данные по выбранному столбцу со значением больше 1.400


# df = pd.read_csv("csv_files/hh.csv")

# df['Test'] = [new for new in range(29)] # добавили столбец
# print(df)

# df.drop('Test', axis=1, inplace=True) #  удаляем объект, который указываем; axis=1 - удаление столбцов, axis=0 - удаление строк; inplace=True - изменения вносятся в исходный дата фрэйм, inplace=False - возвращается измененный дата фрэйм, оригинальный не меняется
# print(df)

# print(df)
# df.drop(28, axis=0, inplace=True) #  удаляем объект, который указываем; axis=1 - удаление столбцов, axis=0 - удаление строк; inplace=True - изменения вносятся в исходный дата фрэйм, inplace=False - возвращается измененный дата фрэйм, оригинальный не меняется
# print(df)



# df = pd.read_csv("csv_files/animal.csv")
# print(df)

# df.fillna(0, inplace=True) # fillna - эта команда заполнит пропуски значением из value
# print(df)
#
# df.dropna(inplace=True) # dropna - эта команда удалит строки в которых значение NaN

# group = df.groupby('Пища')['Средняя продолжительность жизни'].mean() # группируем по значению, затем высчитываем среднее с помощью"mean()"
# print(group)



data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 22, 34, 42],
    'City': ['New York', 'Paris', 'London', 'Berlin']
}

df = pd.DataFrame(data)

df.to_csv('output.csv', index=False) # создаем новый файл csv