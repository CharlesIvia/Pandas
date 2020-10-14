import pandas as pd

df = pd.read_csv("../data/survey_results_public.csv", index_col="Respondent")
schema_df = pd.read_csv("../data/survey_results_schema.csv", index_col="Column")

# pd.set_option("display.max_columns", 85)
# pd.set_option("display.max_rows", 85)

print(df)
print(schema_df)

print(df.shape)

print(df.head())  # first five

# Indexing rows

print(schema_df.loc["Hobbyist"])
print(schema_df.loc["MgrIdiot", "QuestionText"])

# print(schema_df.sort_index())

schema_df.sort_index(ascending=False, inplace=True)
print(schema_df)
