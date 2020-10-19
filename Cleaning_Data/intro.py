import pandas as pd
import numpy as np

people = {
    "first": ["Corey", "Jane", "John", "Chris", np.nan, None, "NA"],
    "last": ["Schafer", "Doe", "Doe", "Schafer", np.nan, np.nan, "Missing"],
    "email": [
        "CoreyMSchafer@gmail.com",
        "JaneDoe@email.com",
        "JohnDoe@email.com",
        None,
        np.nan,
        "Anonymous@email.com",
        "NA",
    ],
    "age": ["33", "55", "63", "36", None, None, "Missing"],
}

df = pd.DataFrame(people)
print(df)

# CUSTOM missing values

df.replace("NA", np.nan, inplace=True)
df.replace("Missing", np.nan, inplace=True)
print(df)

# Removing missing values

print(df.dropna())


print(df.dropna(axis="index", how="any"))

print(df.dropna(axis="columns", how="all"))

# Drop value in a spepecific row and column e. without an email
print(df.dropna(axis="index", how="any", subset=["email"]))

# Drop w/o email  and last
print(df.dropna(axis="index", how="all", subset=["last", "email"]))

print(df.isna())

# Fillna

# df = df.fillna("MISSING")
df.fillna(0)
print(df)

# Casting data types
print(df.dtypes)

df["age"] = df["age"].astype(float)
print(df["age"])
print(df.dtypes)

print(df["age"].mean())

# cast the whole database

# df.astype()
