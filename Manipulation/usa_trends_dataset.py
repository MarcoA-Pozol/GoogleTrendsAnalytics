import pandas as pd
from Utils.get_dataset_chunk import get_dataset_chunk

df = pd.read_csv('./Datasets/usa_week18_trends.csv')

# Get dataset chunk
print(get_dataset_chunk(filepath='./Datasets/usa_week18_trends.csv', chunknumber=4, chunksize=100, viewallrows=True, viewallcolumns=False))
