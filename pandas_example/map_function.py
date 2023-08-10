import pandas as pd
from random import randint

nums = [randint(-5, 5) for i in range(10)]
s = pd.Series(nums)
print(s)
print('--------------------------')

print(s.map(lambda x: x * 2))
