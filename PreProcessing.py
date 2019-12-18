#importing lib
import pandas as pd
#read csv
df = pd.read_csv("Data_2015_1.csv")
#selecting necessary column
df1 = df.iloc[:,1:4]
#renaming columns
df1.columns = ['Date','Tickers','Price']
#Dropping treasury bill rows
df1 = df1[~df1.Tickers.str.contains('|'.join(['T05Y','T10Y','T15Y','T20Y','T5Y']))]
#Converting Price column to String -> Remove ',' -> Convert to Float
df1.Price = pd.to_numeric(df1.Price.astype(str).str.replace(',',''), errors='coerce')
#Pivot table to Desired Dataset
df2= pd.pivot_table(df1, values='Price', index=['Date'], columns='Tickers')
#Save Dataset
df2.to_csv("New_Data_2015_1.csv")