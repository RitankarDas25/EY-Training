import pandas as pd

#step 1:ETL(extraction transformation loading)- extraction
df = pd.read_csv("students.csv")

#step 2 - transformation - clean and calculate
df.dropna(inplace=True) #remove missing rows
df["Marks"]=df["Marks"].astype(int) # convert marks from string to int
df["Result"]=df["Marks"].apply(lambda x: "Pass" if x > 50 else "Fail") # add a coluumn results

#step 3 - Load - save the transformed data
df.to_csv("cleaned_students.csv", index=False)

print("Data pipeline completed.Cleaned data saved to cleaned_students.csv")