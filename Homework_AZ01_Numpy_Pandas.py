import pandas as pd
# import kagglehub



# 1. Скачайте любой датасет с сайта https://www.kaggle.com/datasets
# Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe()).



# path = kagglehub.dataset_download("jockeroika/life-style-data")
# print("Path to dataset files:", path)

# df = pd.read_csv(r'C:\Users\enack\.cache\kagglehub\datasets\jockeroika\life-style-data\versions\7\meal_metadata.csv')
# print(df.head())
# print(df.info())
# print(df.describe())



# 2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

df = pd.read_csv('csv_files/dz.csv')
print(df)
df.fillna(0, inplace=True)
print(df)


middle_salary = df.groupby('City')['Salary'].mean()
print(middle_salary)
df.to_csv('output_Homework_AZ01_Numpy_Pandas.csv', index=False)

