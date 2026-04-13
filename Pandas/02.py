# A DataFrame in pandas is a two-dimensional table of data with rows and columns.

# Think of it like:
# 👉 an Excel sheet or a database table inside Python.

# Key features:
# Has rows (index) and columns (labels)
# Each column can have a different data type
# Built from lists, dictionaries, NumPy arrays, or files (like CSV)

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}

df = pd.DataFrame(data)
print(df)