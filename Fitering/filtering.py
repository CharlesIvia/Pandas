import pandas as pd

df = pd.read_csv("../data/survey_results_public.csv", index_col="Respondent")
schema_df = pd.read_csv("../data/survey_results_schema.csv", index_col="Column")

# pd.set_option("display.max_columns", 85)
# pd.set_option("display.max_rows", 85)

print(df)
print(schema_df)

print(df.shape)

print(df.head())  # first five

# Filter salary abv certain amount

high_salary = df["ConvertedComp"] > 80000
high_sal = df.loc[high_salary, ["Country", "LanguageWorkedWith", "ConvertedComp"]]
print(high_sal)


# filter by country
countries = ["United States", "India", "United Kingdom", "Germany", "Canada"]

filt = df["Country"].isin(countries)
print(df.loc[filt, "Country"])

# Dev work with a specific language

filt = df["LanguageWorkedWith"].str.contains("Python", na=False)
print(filt)
print(df.loc[filt, "LanguageWorkedWith"])
