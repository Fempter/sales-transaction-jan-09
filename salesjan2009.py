import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv("SalesJan2009.csv", parse_dates=["Transaction_date", "Account_Created", "Last_Login"], skip_blank_lines=True)
df['City'] = df['City'].str.strip()
df['Price'] = df.Price.str.replace(',','.').str.replace('"','')
df['Price'] = pd.to_numeric(df['Price'])
#print(df.head(4), end='\n\n\n')

#b = df.between_time("17:00", "18:00")
#print(b)

#print(df.dtypes)

plt.hist(df['Price'])
plt.show()