#importing lib
import pandas as pd
import os

#Path to Datasets you want to batch process
path = '/Users/shahriyer/Desktop/code/Datasets/'
#Path for Saving Processed Datasets
new_path = '/Users/shahriyer/Desktop/code/New_Datasets/'

#Make List of .csv file names
filename = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            filename.append(file)

#Sort list Alphabetically
filename.sort()

for i in filename:
    #read csv
    df = pd.read_csv(path+i)
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
    df2.to_csv(new_path+"New_"+i)

