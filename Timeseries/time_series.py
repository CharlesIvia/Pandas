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

# Datename of entire column/series

date_names = df["Date"].dt.day_name()
print(date_names)

# Create new column

df["DayOfWeek"] = date_names
print(df)

# Earliest and latest date

earliest = df["Date"].min()
most_recent = df["Date"].max()

print(earliest)
print(most_recent)

# TimeDelta

tm_delta = most_recent - earliest
print(tm_delta)

# Filters

filt = df["Date"] >= "2020"
print(df.loc[filt])

filt = (df["Date"] >= "2019") & (df["Date"] < "2020")
print(df.loc[filt])

# Alternative filters

filt = (df["Date"] >= pd.to_datetime("2019-01-01")) & (
    df["Date"] < pd.to_datetime("2020-01-01")
)
print(df.loc[filt])

# Set index to Date
df.set_index("Date", inplace=True)
print(df)

# Data for 2019

# data_2019 = df["2019"]
# print(data_2019)

# Data on daily basis
