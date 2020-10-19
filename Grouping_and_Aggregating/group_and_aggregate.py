from numpy.lib.function_base import median
import pandas as pd

df = pd.read_csv("../data/survey_results_public.csv", index_col="Respondent")
schema_df = pd.read_csv(
    "../data/survey_results_schema.csv", index_col="Column")

# pd.set_option("display.max_columns", 85)
# pd.set_option("display.max_rows", 85)

print(df)
print(schema_df)

print(df.shape)

#Basic aggregarions- mean, medium and mode

#Typical sal of developers

sals = df["ConvertedComp"].head(15)
print(sals)

median_sals = sals.median()
print(median_sals)

#Running aggregate fns on entire df
print(df.median())

print(df.describe())  # can be ran for specific column


#No of responses to converted comp

comp_count = df["ConvertedComp"].count()
print(comp_count)

#Total of different responses to a question in a column

hobb_diff = df["Hobbyist"].value_counts()
print(hobb_diff)

#Popular answers to social media question
social_qs = schema_df.loc["SocialMedia"]
print(social_qs)

pop_social = df["SocialMedia"].value_counts()
print(pop_social)

#By percentage
pop_social = df["SocialMedia"].value_counts(normalize=True)
print(pop_social)
