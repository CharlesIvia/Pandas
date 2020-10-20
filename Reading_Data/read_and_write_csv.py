import pandas as pd

# READ CSV

df = pd.read_csv("../data/survey_results_public.csv", index_col="Respondent")
schema_df = pd.read_csv("../data/survey_results_schema.csv", index_col="Column")

print(df)
print(schema_df)

# WRITE CSV

filt = df["Country"] == "Kenya"
kenya_df = df.loc[filt]
print(kenya_df.head(20))

kenya_df.to_csv("./data/kenyan_data.csv")
