import pandas as pd

# Create DataFrame from Dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 40, 33]}

df = pd.DataFrame(data)
print(df)

# print only two 2 rows
print(df.head(2))

# print info about df
print(df.info)

# calculate a average age
average_age_from_df = df['Age'].mean()
print(f"Average age : {average_age_from_df}")

# save result to CSV file
# df.to_csv('example_save_result.csv', index=False)
# df.to_csv('example_save_result_with_index.csv', index=True)

df.to_json('example_save_result.json', orient='records')
