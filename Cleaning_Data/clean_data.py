import pandas as pd


na_vals = ["NA", "Missing"]
df = pd.read_csv(
    "../data/survey_results_public.csv", index_col="Respondent", na_values=na_vals
)
schema_df = pd.read_csv("../data/survey_results_schema.csv", index_col="Column")


print(df)
print(schema_df)

print(df.head())  # first five

# view unique values. Recall that to count unique values use value_count

print(df["YearsCode"].unique())

# Calculate years of coding experience
df["YearsCode"].replace("Less than 1 year", 0, inplace=True)
df["YearsCode"].replace("More than 50 years", 51, inplace=True)

print(df["YearsCode"].unique())

df["YearsCode"] = df["YearsCode"].astype(float)
years_exp = df["YearsCode"]

print(years_exp.mean())
print(years_exp.median())
