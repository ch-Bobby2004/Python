import numpy as np 
import pandas as pd 

df1 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})
print(df1)
print()
print(df1.shape)
print()
print(df1.columns)
print()
print(df1.info())
print()
print(df1.describe())
print()
print(df1['A'] + 10)
print()
print(df1)
print()
ak = df1['D'] = df1["B"].apply(lambda x : x**2)
print(ak)
print(df1)