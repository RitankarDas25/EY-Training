import pandas as pd
import numpy as np
data = {
    "Name": ["Rahul","Priya","Arjun"],
    "Age":[21,22,20],
    "Courses":["Ai","ML","Data Science"],
    "Marks":[85,90,78]
}
df = pd.DataFrame(data)
print(df)

#selecting data
print(df["Name"]) #single column
print(df[["Name","Age"]]) # multiple columns
print(df.iloc[0]) #1st row
print(df.loc[2,"Marks"]) #value at row 2,column marks

#filter data
high_scores=df[df["Marks"]>85]
print(high_scores)

#add columns
df["Results"]=np.where(df["Marks"]>=80,"Pass","Fail")

#update data
df.loc[df["Name"]== "Rahul","Marks"]=80
print(df)

