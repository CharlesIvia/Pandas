import pandas as pd

df = pd.read_csv("../data/survey_results_public.csv")
print(df)

print(df.shape)
print(df.info())