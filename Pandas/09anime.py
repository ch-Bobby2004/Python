
import numpy as np 
import pandas as pd 
df = pd.read_csv(r'anime.csv')
# print(df)
print()
# df.head() returns the first 5 rows of the DataFrame by default.
print(df.head()) 
print()
print(df.loc[4]['Title'])
print()


#make a new column for episode count
def extract_episodes(txt):
    check = False
    data = ""
    for i in txt:
        if i == ")":
            check = False
            return data
        if check == True: 
            data = data + i 
        if i == '(':
            check = True 

df["Episodes"] = df["Title"].apply(extract_episodes)
df['Episodes']= df['Episodes'].str.replace(" eps","")
df['Episodes'] = df['Episodes'].astype(int)
print(df.head())
print()


#make a new column for time stamp
print(df.loc[3]['Title'])

def extraction_time(txt):
    check = False
    data = ""
    for i in range(len(txt)):
        if txt[i] == ')':
            for j in range(i+1,i+20):
                data += txt[j]

            return data

df['Total Time'] = df['Title'].apply(extraction_time)
print(df.head())
print()



from dateutil.relativedelta import relativedelta
from datetime import datetime

def calculate_total_months(period):
    try:
        start_str, end_str = period.split(' - ')
        start_date = datetime.strptime(start_str, '%b %Y')
        end_date = datetime.strptime(end_str, '%b %Y')
        r = relativedelta(end_date, start_date)
        return r.years * 12 + r.months + 1 
    except:
        return None

df['Months'] = df['Total Time'].apply(calculate_total_months)
print(df.head())

# which anime has the highest score
print(df[df['Score'] == df['Score'].max()]['Title'])

# which anime has the highest episode count
print(df[df['Episodes'] == df['Episodes'].max()])