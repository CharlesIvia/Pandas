import pandas as pd

person = {"first": "Corey", "last": "Schafer", "email": "CoreyMSchafer@gmail.com"}

people = {"first": ["Corey"], "last": ["Schafer"], "email": ["CoreyMSchafer@gmail.com"]}

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
}

# print(people["email"])

# Convert a dic into a df- keys become columns

df = pd.DataFrame(people)
print(df)

# Updating rows and columns

# UPDATING COLUMNS

columns = df.columns
print(columns)

# All columns
df.columns = ["first_name", "last_name", "email"]
print(df)

# Change sth specific in columns

df.columns = [x.lower() for x in df.columns]
print(df)

df.columns = df.columns.str.replace(" ", "_")
print(df)

# Change some columns

df.rename(columns={"first_name": "first", "last_name": "last"}, inplace=True)
print(df)


# UPDATING ROWS

df.loc[2] = ["John", "Smith", "jsmith@gmail.com"]
print(df)


# Updating specific column from row

df.loc[2, ["last", "email"]] = ["Doe", "JohnDoe@gmail.com"]
print(df)

# Single value

df.loc[2, "last"] = "Smith"
print(df)

# Single calue using at

df.at[2, "last"] = "Doe"
print(df)

filt = df["email"] == "JohnDoe@gmail.com"
print(df[filt])
df.loc[filt, "last"] = "Smith"
print(df)


# Updating multiple rows

# Make all emails lowercase

df["email"] = df["email"].str.lower()
print(df)

# apply, map, applymap and replace

# apply for a series (used to apply fns)

print(df["email"].apply(len))


def update_email(email):
    return email.upper()


df["email"] = df["email"].apply(update_email)
print(df)

df["email"] = df["email"].apply(lambda x: x.lower())
print(df)

# apply with dataframes

print(df["email"].apply(len))
print(df.apply(len))


# applymap- works on each element

print(df.applymap(str.lower))

# map - subsitute series element with another

print(df["first"].map({"Corey": "Chris", "Jane": "Mary"}))

# replace

df["first"] = df["first"].replace({"Corey": "Chris", "Jane": "Mary"})
print(df)
