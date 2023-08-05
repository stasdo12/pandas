import pandas as pd

a = [1, 2, 4, 55, 65]

series_example = pd.Series(a)
print(series_example)
print(series_example[0])

series_with_range = pd.Series(range(0, 100, 5))
print(series_with_range)

# How to change index in our elements?  number index continue stay
words = ['Hello', 'World']
string_series = pd.Series(words, ["Привет", "Мир"])
print(string_series)
print(string_series["Привет"])

# Make series from dictionary with our keys (String this is Object)
dictionary = {"Привет": "Hello", "Мир": "World", "Пайтон лучший": "Python Best"}
dict_example = pd.Series(dictionary)
print(dict_example)

