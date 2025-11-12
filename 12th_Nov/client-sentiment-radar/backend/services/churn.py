import pandas as pd
import numpy as np

def add_churn_scores(df):
    df["churn_risk"] = np.where(df["sentiment"] == "NEGATIVE",
                                np.random.uniform(0.6, 1.0, len(df)),
                                np.random.uniform(0.0, 0.5, len(df)))
    return df

def aggregate_by_client(df):
    return df.groupby("sentiment")["churn_risk"].mean().to_dict()
