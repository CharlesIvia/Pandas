import pandas as pd

# READ CSV

df = pd.read_csv("../data/survey_results_public.csv", index_col="Respondent")
schema_df = pd.read_csv("../data/survey_results_schema.csv", index_col="Column")

print(df)
print(schema_df)

# WRITE EXCEL

filt = df["Country"] == "India"
india_df = df.loc[filt]
print(india_df.head(20))

india_df.to_excel("../data/india_data_exel.xlsx")


test = pd.read_excel("../data/india_data_exel.xlsx", index_col="Respondent")

print(test)
