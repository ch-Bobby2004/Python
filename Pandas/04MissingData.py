import numpy as np 
import pandas as pd 
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan],
    'D': [1, np.nan, np.nan, np.nan, 5]
}
# np → NumPy
# nan → Not a Number
# So np.nan = a blank / missing value placeholder

df = pd.DataFrame(data)
print(df)
# True → value is missing (NaN)
# False → value is present

print(df.isna())

print(df.isna().sum())  #Counting missing values per column
# .isna() → shows where data is missing
# .sum() → counts missing values

print()
print(df.isna().any())
# Checks each column
# Returns True if at least one NaN exists in that column
print()
print(df.dropna())
# dropna() removes: base on row
# Any row that contains at least one NaN value (by default)

print()
print(df.dropna(thresh=3))  
# thresh = minimum number of non-NaN values required to keep a row/column

print()
print(df.fillna(0)) #Replace all NaN (missing values) with 0

print()

values = {'A':0,'B':100,"C":300,'D':400}
print(df.fillna(value=values))

print()

print(df.fillna(df.mean()))  #calculates the mean (average) of each column

# To make all changes permanent in pandas, you have 2 main ways
# Reassign the result
df = df.dropna()
# using inplace
df.dropna(inplace=True)