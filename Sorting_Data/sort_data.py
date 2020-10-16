import pandas as pd

df = pd.read_csv("../data/survey_results_public.csv")
schema_df = pd.read_csv("../data/survey_results_schema.csv")

# pd.set_option("display.max_columns", 85)
# pd.set_option("display.max_rows", 85)

print(df)
print(schema_df)

# Sorting Data

# sort by country and salary

df.sort_values(by=["Country", "ConvertedComp"], ascending=[True, False], inplace=True)
print(df[["Country", "ConvertedComp"]].head(50))

# Other methods

# nlargest on series

largest_sals = df["ConvertedComp"].nlargest(10)
print(largest_sals)

# On a df

df_sorted_large_sal = df.nlargest(10, "ConvertedComp")
print(df_sorted_large_sal)

df_sorted_small_sal = df.nsmallest(10, "ConvertedComp")
print(df_sorted_small_sal)
