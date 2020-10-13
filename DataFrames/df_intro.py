import pandas as pd

person = {"first": "Corey", "last": "Schafer", "email": "CoreyMSchafer@gmail.com"}

people = {"first": ["Corey"], "last": ["Schafer"], "email": ["CoreyMSchafer@gmail.com"]}

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
}

print(people["email"])

# Convert a dic into a df

df = pd.DataFrame(people)
print(df)

emails = df["email"]
print(emails)
print(type(emails))  # series

# dot notation-not preferred

print(df.email)

# Accessing several colums

print(df[["last", "email"]])

# All columns

print(df.columns)

# Rows- iloc/interger-location or loc

print(df.iloc[0])


# multiple rows

print(df.iloc[[0, 1]])

# Coulumns from rows

print(df.iloc[[0, 1], 2])


# loc- searches by labels

print(df.loc[0])

# multiple rows

print(df.loc[[0, 1]])

# columns from rows

print(df.loc[[0, 1], ["email", "last"]])
