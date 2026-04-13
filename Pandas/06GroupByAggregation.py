import numpy as np 
import pandas as pd 

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store': ['S1', 'S1', 'S2', 'S2', 'S1', 'S2', 'S2', 'S1'],
    'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
    'Date': pd.date_range('2023-01-01', periods=8)
}
df = pd.DataFrame(data)
print(df)
print()
cat = df.groupby('Category')['Sales'].sum()
print(cat)
print()
cat = df.groupby('Store')['Sales'].sum()
print(cat)
print()
cat = df.groupby(['Category','Store'])['Sales'].sum()
print(cat)

print()
print(df['Sales'].mean())
print()
# Aggregation 
print(df['Sales'].agg(['sum', 'mean', 'min', 'max', 'count', 'std', 'median']))