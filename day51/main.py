import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("day51/QueryResults.csv", header=0, names=['DATE', 'TAG', 'POSTS'])
df = df.dropna()
df["DATE"] = pd.to_datetime(df["DATE"])

num_of_posts = df.groupby("TAG").sum().sort_values("POSTS", ascending=False)
print(num_of_posts)

num_of_posts_month = df.groupby(["TAG"]).count()
print(num_of_posts_month)

reshaped_df = df.pivot(index="DATE", columns=["TAG"], values=["POSTS"]).fillna(0)
nan_values = reshaped_df.isna().values.any()
print(reshaped_df.head())
print(reshaped_df.columns)


plt.figure(figsize=(16,10))
plt.ylabel("Anzahl Posts", fontsize=14)
plt.ylim(0, 35000)
plt.xlabel("Jahr", fontsize=14)

for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], linewidth=3, label=reshaped_df[column].name[1])
plt.legend(fontsize=16) 

plt.show()


roll_df = reshaped_df.rolling(window=12).mean()
plt.figure(figsize=(16,10))
plt.ylabel("Anzahl Posts", fontsize=14)
plt.ylim(0, 35000)
plt.xlabel("Jahr", fontsize=14)

for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=roll_df[column].name[1])
plt.legend(fontsize=16) 

plt.show()