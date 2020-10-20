import pandas as pd
import datetime as dt

d_parser = lambda x: dt.datetime.strptime(x, "%Y-%m-%d %I-%p")
df = pd.read_csv("./data/ETH_1h.csv", parse_dates=["Date"], date_parser=d_parser)

print(df.head())
print(df.shape)

# DATES

# test = df.loc[0, "Date"].day_name()

# Convert column to date_time

# df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d %I-%p')

# print(df["Date"])

test = df.loc[0, "Date"].day_name()
print(test)
