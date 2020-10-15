import pandas as pd

df = pd.read_csv("../data/survey_results_public.csv", index_col="Respondent")
schema_df = pd.read_csv("../data/survey_results_schema.csv", index_col="Column")

# pd.set_option("display.max_columns", 85)
# pd.set_option("display.max_rows", 85)

print(df)

print(df.rename(columns={"ConvertedComp": "SalaryUSD"}, inplace=True))
print(df["SalaryUSD"])

# Map

df["Hobbyist"] = df["Hobbyist"].map({"Yes": True, "No": False})
print(df["Hobbyist"])
