import pandas as pd

df = pd.read_csv("../data/survey_results_public.csv")
schema_df = pd.read_csv("../data/survey_results_schema.csv")

# pd.set_option("display.max_columns", 85)
# pd.set_option("display.max_rows", 85)

print(df)
print(schema_df)

print(df.shape)

hobbyist = df["Hobbyist"]
print(hobbyist)

# Unique values

unique_res = df["Hobbyist"].value_counts()
print(unique_res)

# Grabbing rows

print(df.loc[0])
print(df.loc[0, "Hobbyist"])

# Grabbbing multiple rows

print(df.loc[[0, 1, 2], "Hobbyist"])

# Using slicing

print(df.loc[0:2, "Hobbyist":"Employment"])
