import pandas

data = pandas.read_csv("day25/great_squirrel_data.csv")

new_data = data["Primary Fur Color"].value_counts().to_frame()
new_data.columns = ["Color count"]
print(new_data)