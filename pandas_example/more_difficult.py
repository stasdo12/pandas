import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', ''],
        'Age': [25, 30, 22, 10]}

data1 = {'Name': ['Cevin', 'Soll', 'Cristian', ''],
         'Age': [22, 21, 22, 23]}
data2 = {'Department': ['Brussels', 'Kharkov', 'Oslo', 'Budapest'],
         'Cost': [2233, 2122, 2233, 2333]}

data3 = {'Name': ['Alice', 'Bob'],
         'Age': [25, 30],
         'Date': ['2023-08-01', '2023-08-02']}

df = pd.DataFrame(data)
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data1)
df3 = pd.DataFrame(data2)
df4 = pd.DataFrame(data3)
print("______________________________________")
# Certain statistics (mean, standard deviation, etc.)
print(df.describe())
print("______________________________________")
# choose a column by name
names = df['Name']
print(names)
print("______________________________________")
# choose rows by index
row = df.loc[1]
print(row)
print("______________________________________")
# filtering
filtered_df = df[df['Age'] > 25]
print(filtered_df)
print("______________________________________")
# Grouping by column and calculating averages
grouped = df.groupby('Age')['Age'].mean()
print(grouped)
print("______________________________________")
# Add new column
# df['City'] = ['New York', 'London', 'Paris']
# print(df)
print("______________________________________")
# Drop a column
# df = df.drop(columns='City')
# print(df)
print("______________________________________")
# Read from the file CSV
csv_df = pd.read_csv('example_save_result.csv')
print(csv_df)
print("______________________________________")
# Read from the file CSV
# xml_df = pd.read_xml('example.xlsx')
print("______________________________________")
# Counting null values in a DataFrame
print(df.isnull().sum())

print("______________________________________")
# Sort Ascending
sorted_df = df.sort_values(by="Name")
print(sorted_df)
print("______________________________________")

# Join by rows (vertical)
merged_df = pd.concat([df1, df2])
print(merged_df)
print("______________________________________")
# Join by rows (horizontal)
merged_columns_df = pd.concat([df1, df3], axis=1)
print(merged_columns_df)
print("______________________________________")
# Convert column to date format
df4['Date'] = pd.to_datetime(df4['Date'])
print(df4)
print("______________________________________")
df4['Year'] = df4['Date'].dt.year
print(df4)