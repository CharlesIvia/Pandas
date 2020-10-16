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

# Adding Columns to dataframes

full_name = df["first"] + " " + df["last"]
print(full_name)

df["full_name"] = full_name
print(df)


# Remove columns

df.drop(columns=["first", "last"], inplace=True)
print(df)

# Split full_name into two coumns

split_full_name = df["full_name"].str.split(" ", expand=True)

df[["first", "last"]] = split_full_name
print(df)

# Adding and removing rows of data

# Adding a single row of data

print(df.append({"first": "Tony"}, ignore_index=True))


people_two = {
    "first": ["Tony", "Steve"],
    "last": ["Stark", "Rogers"],
    "email": ["iron@gmail.com", "steve@gmail.com"],
}

df2 = pd.DataFrame(people_two)
print(df2)

df = df.append(df2, ignore_index=True)
print(df)

# Removing rows

df.drop(index=4, inplace=True)
print(df)

# Drop rows conditionally e.g all with last_name as Doe

filt = df["last"] == "Doe"

df = df.drop(index=df[filt].index)
print(df)
