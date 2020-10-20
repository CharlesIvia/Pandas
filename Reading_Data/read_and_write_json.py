import pandas as pd

# READ CSV

df = pd.read_csv("../data/survey_results_public.csv", index_col="Respondent")
schema_df = pd.read_csv("../data/survey_results_schema.csv", index_col="Column")

print(df)
print(schema_df)

# WRITE JSOn

filt = df["Country"] == "India"
india_df = df.loc[filt]
print(india_df.head(20))

india_df.to_json("../data/india_data_json.json")
india_df.to_json("../data/india_data_json_list.json", orient="records", lines=True)


# READ JSON

test = pd.read_json("../data/india_data_json_list.json", orient="records", lines=True)
print(test)
