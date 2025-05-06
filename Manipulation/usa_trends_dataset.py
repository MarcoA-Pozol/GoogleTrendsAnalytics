import pandas as pd
import sqlite3
from Utils.get_dataset_chunk import get_dataset_chunk

conn = sqlite3.connect('Trends2025.db')

df = pd.read_csv('./Datasets/usa_week18_trends.csv')

# Get dataset chunk
df = get_dataset_chunk(filepath='./Datasets/usa_week18_trends.csv', chunknumber=4, chunksize=100, viewallrows=False, viewallcolumns=True)

# Save dataframe as sql table
df.to_sql('UsaTrends', conn, if_exists='replace', index=False)

# Top 10 most popular trends by search volume in USA
query = 'SELECT Trends, "Search volume" FROM UsaTrends ORDER BY "Search volume" DESC LIMIT 10;'
result = pd.read_sql(query, conn)

print(result)


# Top 10 less popular trends by search volume in USA
query = 'SELECT Trends, "Search volume" from UsaTrends ORDER BY "Search volume" ASC LIMIT 10;'
result = pd.read_sql(query, conn)
print(result)
