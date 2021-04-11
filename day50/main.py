import pandas as pd


pd.options.display.float_format = '{:,.2f}'.format 

df = pd.read_csv("day50/salaries_by_college_major.csv")

clean_df = df.dropna()

print(clean_df.columns)

max_starting_sal = clean_df["Starting Median Salary"].max()
max_starting_sal_id = clean_df["Starting Median Salary"].idxmax()
max_starting_row = clean_df.loc[max_starting_sal_id]

print(max_starting_row)

max_mid_sal = clean_df["Mid-Career Median Salary"].max()
max_mid_sal_id = clean_df["Mid-Career Median Salary"].idxmax()
max_mid_row = clean_df.loc[max_mid_sal_id]

print(max_mid_row)

min_starting_sal = clean_df["Starting Median Salary"].min()
min_starting_sal_id = clean_df["Starting Median Salary"].idxmin()
min_starting_row = clean_df.loc[min_starting_sal_id]

print(min_starting_row)

min_mid_sal = clean_df["Mid-Career Median Salary"].min()
min_mid_sal_id = clean_df["Mid-Career Median Salary"].idxmin()
min_mid_row = clean_df.loc[min_mid_sal_id]

print(min_mid_row)

mid_salary_dif = clean_df["Mid-Career 90th Percentile Salary"].subtract(clean_df["Mid-Career 10th Percentile Salary"])
clean_df.insert(1, "Spread", mid_salary_dif)
print(clean_df.sort_values("Spread").head())

print(clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False).head())
print(clean_df.sort_values("Spread", ascending=False).head())


print(clean_df.groupby("Group").count())
print(clean_df.groupby("Group").mean())