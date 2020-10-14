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
#print(df)

#print(df["email"])

#Set email as index

df.set_index("email", inplace=True)
print(df)

print(df.index)

#Accessing rows

print(df.loc["CoreyMSchafer@gmail.com"])
print(df.iloc[0])


#Reseting index

df.reset_index(inplace=True)
print(df)