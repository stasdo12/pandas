import pandas as pd
from random import randint, shuffle, choice
from string import ascii_lowercase

numbers = [randint(-50, 50) for i in range(26)]
series_numbers = pd.Series(numbers)
print(series_numbers)

# index call
print(series_numbers[4])
print("-------------------------------")
# slicing
print(series_numbers[:10])
print("-------------------------------")
print(series_numbers[10:])
print("-------------------------------")
print(series_numbers[:])
print("-------------------------------")
# we can add step
print(series_numbers[:10:-1])
print("-------------------------------")
print("-------------------------------")
print("-------------------------------")
# if we have a string index
ind = list(ascii_lowercase)
series_numbers_letter_index = pd.Series(numbers, ind)
print(series_numbers_letter_index)
print("-------------------------------")
print(series_numbers_letter_index['a':'f'])
# we can shuffle our latters
shuffle(ind)
print(ind)
series_numbers_letter_index = pd.Series(numbers, ind)
print(series_numbers_letter_index)
print(series_numbers_letter_index['a':'b'])

# methods loc and iloc
nums = [randint(-50, 50) for z in range(10)]
index_not_unique = [choice([0, 1, 2, 3]) for x in range(10)]
alpha = [choice('abc') for t in range(10)]
print("-------------------------------")
print(alpha)
s = pd.Series(nums)
s_not_unique = pd.Series(nums, index_not_unique)
print(s)
print(s_not_unique)
print("-------------------------------")
# iloc get value by rows number
print(s_not_unique.iloc[[2, 1]])
# loc get values where id = ()
print(s_not_unique.loc[[1, 2, 3]])
# we can change values in our series
s_not_unique.loc[3] = 25
print(s_not_unique)
s_not_unique_with_latter_index = pd.Series(nums, alpha)
print(s_not_unique_with_latter_index)
print(s_not_unique_with_latter_index.iloc[[1, 3]])
print(s_not_unique_with_latter_index.loc[['a', 'b']])
