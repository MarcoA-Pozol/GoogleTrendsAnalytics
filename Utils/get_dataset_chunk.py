import pandas as pd

def get_dataset_chunk(filepath:str, chunknumber:int=1, chunksize:int=50, viewallrows:bool=False, viewallcolumns:bool=False) -> pd.DataFrame:
    """
        Get an specified chunk of data from a dataframe.

        Args:
        - filepath (str): Path of the file in csv or xlsx format
        - chunknumber (int): Number of chunk the user wants to get
        - chunksize (int): Number of rows of the chunk
        - viewallrows (bool): Display all rows of the chunk in console view
        - viewallcolumns (bool): Display all columns of the chunk in console view
    """

    # Validated filepath extension
    if not filepath.endswith(('.csv', '.xls', '.xlsx')):
        raise ValueError(f'Filepath must contain a value file extension (csv, xls, xlsx)')
    
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    if filepath.endswith('.xlsx') or filepath.endswith('.xls'):
        df = pd.read_excel(filepath)

    # Split dataframe into chunks with the size of chunksize each one
    chunks = [df.iloc[i:i+chunksize] for i in range(0, len(df), chunksize)]

    # Get selected chunk
    df_chunk = chunks[chunknumber]

    # Setup for rows and columns displaying
    if viewallrows:
        pd.set_option('display.max_rows', df.shape[0])
    if viewallcolumns:
        pd.set_option('display.max_columns', df.shape[1])

    return df_chunk