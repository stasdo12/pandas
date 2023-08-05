import pandas as pd

names = ['Stan', 'Bob', 'Kevin', 'Robin']
letters = "b", "j", "k", "r"
numbers = [10, 20, 30, 40, 50]

# All are object of the series
names_example = pd.Series(names)
number_example = pd.Series(numbers)
s_letters = pd.Series(names, letters)
# Attributes
# Get all values
print(names_example.values)
print(number_example.values)
print('__________________________')
# Index RangeIndex(start=0, stop=4, step=1), Index(['b', 'j', 'k', 'r'], dtype='object')
print(names_example.index)
print(number_example.index)
print(s_letters.index)
# Size
print(number_example.size)
print(names_example.size)

# Is unique
print(number_example.is_unique)

# Is monotonic (return truer if our collection increases or decreasing )
print(number_example.is_monotonic_decreasing)
print(number_example.is_monotonic_increasing)

# ndim return size of dimensions
print(number_example.ndim)

# dtype return type our series
print(number_example.dtype)
print(names_example.dtype)


# methods
