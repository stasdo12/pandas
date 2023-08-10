import pandas as pd
from random import randint, choice
from faker import Faker

# sort_values method
numbers = [randint(-50, 50) for i in range(15)]
series_with_numbers = pd.Series(numbers)
print(series_with_numbers)
print(series_with_numbers.sort_values())
# if we want not change our original series, inplace doesn't change our series if False
print("-------------------------------")
series_with_numbers.sort_values(inplace=False)
print(series_with_numbers)
print("-------------------------------")
series_with_numbers.sort_values(inplace=True)
print(series_with_numbers)
# ascending  sorting order parameter
print(series_with_numbers.sort_values(ascending=True))
print(series_with_numbers.sort_values(ascending=False))

# string sorting in Series
fake = Faker()
print(fake.name())

names = [fake.name() for i in range(15)]
series_names = pd.Series(names)
series_names.sort_values(inplace=True, ascending=False)
print(series_names)

# sort index

numbers_with_name_index = [randint(-50, 50) for i in range(15)]
names_for_series = [fake.name() for i in range(15)]
series_numbers_with_name_index = pd.Series(numbers_with_name_index, names_for_series)
print(series_numbers_with_name_index)
series_numbers_with_name_index.sort_values(inplace=True)
print("---------------------------------")
print(series_numbers_with_name_index)
print("---------------------------------")
print(series_numbers_with_name_index.sort_index(ascending=False))

# sort index date
data = fake.date()
numbers_with_date_index = [randint(-50, 50) for r in range(15)]
date_index = [fake.date() for b in range(15)]
series_with_date = pd.Series(numbers_with_date_index, date_index)
print(series_with_date)
print(series_with_date.sort_index())
print("---------------------------------")
print("---------------------------------")
print("---------------------------------")

# method value_counts()

numbers_for_count_method = [randint(2, 4) for i in range(10)]
alpha = [choice('abc') for t in range(10)]
series = pd.Series(numbers_for_count_method, alpha)
print(series)
v_count = series.value_counts()
print(v_count)

# method apply() we have a 3 types of the number + - 0 we want to create 3 pulls for this

numbers_for_apply_method = [randint(-10, 10) for i in range(75)]
series_for_apply_method = pd.Series(numbers_for_apply_method)
print(series_for_apply_method)


def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    return 'ZERO'


print(series_for_apply_method.apply(sign).head(10))

names_for_apply_method = [fake.name() for i in range(15)]
series_for_apply_method_with_name = pd.Series(names_for_apply_method)
print(series_for_apply_method_with_name)


# if we need to get only surname
def surname(s):
    return s.split()[0]


print(series_for_apply_method_with_name.apply(surname))

# created it with lambda

print(series_for_apply_method_with_name.apply(lambda x: x.split()[1]))
