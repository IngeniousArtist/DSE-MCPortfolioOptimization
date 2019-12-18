#importing lib
import pandas as pd
import os

#Path to Datasets you want to batch process
path = '/Users/shahriyer/Desktop/code/New_Datasets/'
#Path for Saving Processed Datasets
new_path = '/Users/shahriyer/Desktop/code/'

#Make List of .csv file names
filename = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            filename.append(file)

#Sort list Alphabetically
filename.sort()

frames = []
for i in filename:
    #read csv
    df = pd.read_csv(path+i)
    #reset index
    df = df.reset_index()
    #Print shape of df
    print(df.shape)
    #append to list
    frames.append(df)

#concat dataframes
result = pd.concat(frames)
result = result.set_index('Date')

#Print result df shape for cross check
print(result.shape)

result.to_csv(new_path+"Combined_Data.csv")
