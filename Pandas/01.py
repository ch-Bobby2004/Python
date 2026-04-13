# n Pandas, a Series is a one-dimensional labeled array.

# Think of it like a single column in a table, where each value has an associated label (called an index).

# 🔹 Key features of a Series:
# Holds one column of data
# Has index + values
# Can store different data types (numbers, strings, etc.)
# Similar to a list, but with labels



import pandas as pd

data = [10, 20, 30, 40]
s = pd.Series(data)

print(s)
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)


import numpy as np
import pandas as pd

arr = np.array([10, 20, 30, 40])
s = pd.Series(arr)
print(s)
arr = np.random.randn(5)
s = pd.Series(arr)
print(s)


arr = np.array([100, 200, 300])
s = pd.Series(arr, index=["a", "b", "c"])
# labels = ["a", "b", "c"]
# s = pd.Series(arr, index=labels)
print(s)


import pandas as pd

data = {"a": 10, "b": 20, "c": 30}
s = pd.Series(data)

print(s)