import pandas as pd

person = {"first": "Corey", "last": "Schafer", "email": "CoreyMSchafer@gmail.com"}

people = {"first": ["Corey"], "last": ["Schafer"], "email": ["CoreyMSchafer@gmail.com"]}

people = {
    "first": ["Corey", "Jane", "John", "Adam"],
    "last": ["Schafer", "Doe", "Doe", "Doe"],
    "email": [
        "CoreyMSchafer@gmail.com",
        "JaneDoe@email.com",
        "JohnDoe@email.com",
        "A@gmail.com",
    ],
}


# Convert a dic into a df- keys become columns

df = pd.DataFrame(people)

# Sorting data

# sort last name

df.sort_values(by="last", inplace=True)
print(df)
df.sort_values(by="last", ascending=False, inplace=True)
print(df)


# Sorting with multiple conditions

df.sort_values(by=["last", "first"], inplace=True)
print(df)

df.sort_values(by=["last", "first"], ascending=[False, True], inplace=True)
print(df)

# sort_index

df = df.sort_index()
print(df)

# sort single column

df = df["last"].sort_values()
print(df)
