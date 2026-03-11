src/data_preprocessing.py

import pandas as pd

def load_and_preprocess(path):
    df = pd.read_csv(path)

    # Drop unnecessary column
    df = df.drop("customerID", axis=1)

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Remove missing values
    df = df.dropna()

    # Convert categorical variables
    df = pd.get_dummies(df, drop_first=True)

    return df
