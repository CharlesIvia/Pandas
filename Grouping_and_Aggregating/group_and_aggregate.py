from numpy.lib.function_base import median
import pandas as pd

df = pd.read_csv("../data/survey_results_public.csv", index_col="Respondent")
schema_df = pd.read_csv("../data/survey_results_schema.csv", index_col="Column")

# pd.set_option("display.max_columns", 85)
# pd.set_option("display.max_rows", 85)

print(df)
print(schema_df)

print(df.shape)

# Basic aggregarions- mean, medium and mode

# Typical sal of developers

sals = df["ConvertedComp"].head(15)
print(sals)

median_sals = sals.median()
print(median_sals)

# Running aggregate fns on entire df
print(df.median())

print(df.describe())  # can be ran for specific column


# No of responses to converted comp

comp_count = df["ConvertedComp"].count()
print(comp_count)

# Total of different responses to a question in a column

hobb_diff = df["Hobbyist"].value_counts()
print(hobb_diff)

# Popular answers to social media question
social_qs = schema_df.loc["SocialMedia"]
print(social_qs)

pop_social = df["SocialMedia"].value_counts()
print(pop_social)

# By percentage
pop_social = df["SocialMedia"].value_counts(normalize=True)
print(pop_social)


# GROUPING DATA

# groupby fn - split, apply fn , combine


country_responses = df["Country"].value_counts()
print(country_responses)

country_group = df.groupby(["Country"])

us_group = country_group.get_group("United States")
print(us_group)

# alternative- using filter

filt = df["Country"] == "United States"
print(df.loc[filt])
# Popular social media sites by country

pop_us_social = df.loc[filt]["SocialMedia"].value_counts()
print(pop_us_social)

# USING GROUPBY

print(country_group["SocialMedia"].value_counts().head(50))

# Popular social media for India
pop_social_india = country_group["SocialMedia"].value_counts().loc["India"]
print(pop_social_india)

pop_social_china = (
    country_group["SocialMedia"].value_counts(normalize=True).loc["India"]
)
print(pop_social_china)


# Medain salaries

print(country_group["ConvertedComp"].median())

# median salary in kenya

med_kenya = country_group["ConvertedComp"].median().loc["Kenya"]
print(med_kenya)

# running several aggregate fns

print(country_group["ConvertedComp"].agg(["median", "mean"]))

# median and mean for Kenya

med_and_mean_kenya = country_group["ConvertedComp"].agg(["median", "mean"]).loc["Kenya"]

print(med_and_mean_kenya)


# Number of python users in a specific country
filt = df["Country"] == "Kenya"

py_users = df[filt]["LanguageWorkedWith"].str.contains("Python")
print(py_users.sum())

# using groupby to get percentages

total_py_users_per_country = country_group["LanguageWorkedWith"].apply(
    lambda x: x.str.contains("Python", na=False).value_counts(normalize=True)
)
print(total_py_users_per_country)

# percentage of devs who know python

country_respondents = df["Country"].value_counts()
print(country_respondents)

country_pythonistas = country_group["LanguageWorkedWith"].apply(
    lambda x: x.str.contains("Python").sum()
)
print(country_pythonistas)


python_df = pd.concat(
    [country_respondents, country_pythonistas], axis="columns", sort=False
)

python_df.rename(
    columns={"Country": "NumRespondents", "LanguageWorkedWith": "NumKnowsPython"},
    inplace=True,
)
print(python_df)

python_df["PctKnowsPython"] = (
    python_df["NumKnowsPython"] / python_df["NumRespondents"]
) * 100

print(python_df)

# sort_values

python_df.sort_values(by="PctKnowsPython", ascending=False, inplace=True)
print(python_df.head(50))

# pc of pythonistas kenya

print(python_df.loc["Afghanistan"])
