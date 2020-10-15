import pandas as pd

person = {"first": "Corey", "last": "Schafer", "email":
          "CoreyMSchafer@gmail.com"}

people = {"first": ["Corey"], "last": ["Schafer"], "email": [
    "CoreyMSchafer@gmail.com"]}

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"],
}

#print(people["email"])

# Convert a dic into a df- keys become columns

df = pd.DataFrame(people)
print(df)

#Comparison

print(df["last"] == "Doe")

filt = df["last"] == "Doe"
print(filt)

filtered = df[filt]
print(filtered)

#Using .loc

print(df.loc[filt, "email"])

#AND and OR in filtering & and |

#using &

filt = (df["last"] == "Doe") & (df["first"] == "John")
print(df.loc[filt, "email"])

#using or

filt = (df["last"] == "Schafer") | (df["first"] == "John")
print(df.loc[filt, "email"])

#Opposite of filter

filt = (df["last"] == "Schafer") | (df["first"] == "John")
print(df.loc[-filt, "email"])
