from random import randint

import pandas as pd

names = ['Stan', 'Bob', 'Kevin', 'Robin']
letters = "b", "j", "k", "r"
numbers = [1, 20, 30, 40, 50]

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
print('__________________________')
# Size
print(number_example.size)
print(names_example.size)
print('__________________________')
# Is unique
print(number_example.is_unique)
print('__________________________')
# Is monotonic (return truer if our collection increases or decreasing )
print(number_example.is_monotonic_decreasing)
print(number_example.is_monotonic_increasing)
print('__________________________')
# ndim return size of dimensions
print(number_example.ndim)
print('__________________________')
# dtype return type our series
print(number_example.dtype)
print(names_example.dtype)
print('__________________________')
# methods
# Sum method
sum_method = number_example.sum()
sum_method_with_names = names_example.sum()
print(sum_method_with_names)
print(sum_method)
print('__________________________')
# Max min method
print(number_example.max())
print(names_example.max())
print(number_example.min())
print(names_example.min())
print('__________________________')
# Multiply all values
print(number_example.product())
print('__________________________')
# Average methods
print(number_example.mean())
print('__________________________')

# Method with arguments
# Method less than
# Method great that
print(number_example.lt(2))
print(number_example.gt(2))
print('__________________________')
# Equal method
print(number_example.eq(20))
print('__________________________')
# Not equal method
print(number_example.ne(50))
print('__________________________')
# Less equal method
print(number_example.le(50))
print('__________________________')
# Great equal method
print(number_example.ge(50))
print('__________________________')
# Absolute method (return a new Series)
numbers1 = [1, -20, -30, 40, 50]
number_example1 = pd.Series(numbers1)
print(number_example1.abs())
print('__________________________')

# If we have many elements (60 and more)
# Use List Comprehension
many_numbers = [randint(-50, 50) for i in range(100)]
new_numbers_with_many_values = pd.Series(many_numbers)
print(new_numbers_with_many_values)
print('__________________________')
# If we need to get any elements from head default value = 5
print(new_numbers_with_many_values.head(40))
print('__________________________')
# If we need to get any elements from tail default value = 5
print(new_numbers_with_many_values.tail(40))
print('__________________________')
# If we need to get any elements from position or with range

print(new_numbers_with_many_values.take([3, 2, 13, 14]))
print('__________________________')
result_with_range = new_numbers_with_many_values.take(range(12, 55, 5))
print(result_with_range)
print('__________________________')
