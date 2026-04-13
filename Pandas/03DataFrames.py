import numpy as np 
import pandas as pd 
# DataFrame  is multiple series
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}
df = pd.DataFrame(data)
print(df)

# using list
print()
data_list = [
    ['John', 28, 'New York', 65000],
    ['Anna', 34, 'Paris', 70000],
    ['Peter', 29, 'Berlin', 62000],
    ['Linda', 42, 'London', 85000]
]
df2 = pd.DataFrame(data_list)
print(df2)
print()
columns = ["Name","Age","City","Salary"]
df2 = pd.DataFrame(data_list,columns =columns)
print(df2)
print()

print(df2[["Name","City"]])
print()
df2["Designation"] = ["Doctor", "Eng.", "Doctor", "Eng."]
print(df2)
print()
print(df2["Designation"])
print()
# df2 = df2.drop(0, axis=0)  or use df2.drop(0, axis=0, inplace=True)
# print(df2)
print()
print(df2.drop(0, axis=0))
print()
print(df2.drop(df2.columns[0], axis=1))
print()
# What does .loc[[0,1]] mean?
# In pandas:
# .loc[] → label-based selection
# [0, 1] → selects rows with index 0 and 1
print(df2.loc[[0,1]])  #loc = location
print()
# .iloc[] → selects data by position (index number)
# 3 → means 4th row (because indexing starts from 0)
print(df.iloc[3]  )#iloc = index location

print()

print(df.loc[[0,1]][["City","Salary"]])

print()
print(df2[df2["Age"] > 30])

print()
print(df2[(df2["Age"] > 30) & (df2["City"] == 'Paris')])
