import pandas as pd
#---------------------------------------------------------------------------------
#Задача 40: Работать с файлом california_housing_train.csv,
# который находится в папке sample_data. Определить среднюю стоимость дома,
# где кол-во людей от 0 до 500 (population).


# df = pd.read_csv('california_housing_train.csv')
# df2 = df[(df['population']<=500)]
# df2Count = df2['median_house_value'].count()
# df2Sum = df2['median_house_value'].sum()
# df2Average = df2Sum / df2Count
# print(f'Средняя стоимость дома, где кол-во людей от 0 до 500 = {df2Average}')


#---------------------------------------------------------------------------------
#Задача 42: Узнать какая максимальная households в зоне минимального значения population.


# df = pd.read_csv('california_housing_train.csv')

# dfMin = df['population'].min()
# df3 = df[df['population'] == df['population'].min()]['households'].max()
# print(df3)