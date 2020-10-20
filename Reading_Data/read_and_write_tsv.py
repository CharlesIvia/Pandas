import pandas as pd

# READ CSV

df = pd.read_csv("../data/survey_results_public.csv", index_col="Respondent")
schema_df = pd.read_csv("../data/survey_results_schema.csv", index_col="Column")

print(df)
print(schema_df)

# WRITE CSV

filt = df["Country"] == "India"
india_df = df.loc[filt]
print(india_df.head(20))

india_df.to_csv("../data/india_data.tsv", sep="\t")
