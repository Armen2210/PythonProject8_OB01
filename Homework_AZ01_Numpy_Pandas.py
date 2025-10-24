import pandas as pd
# import kagglehub
#
#
# path = kagglehub.dataset_download("jockeroika/life-style-data")
# print("Path to dataset files:", path)

df = pd.read_csv('C:\Users\enack\.cache\kagglehub\datasets\jockeroika\life-style-data\versions\7')
print(df.info())


