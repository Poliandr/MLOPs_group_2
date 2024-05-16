import pandas as pd # Importing the pandas library to work with the tabular dataset


df = pd.read_csv('./e-commerce-dataset/Train.csv') # Load the dataset into a pandas dataframe

def check_column_names(df):
    """
    Check if the 'ID' column is not present in the dataset
    """
    return "ID" not in df.columns

def test_check_column_names():
    """
    Test the 'check_column_names' function
    """
    assert check_column_names(df) == True

def check_duplicates(df):
    """
    Check the number of duplicate rows in the dataset
    """
    return df.duplicated().sum()

def test_check_duplicates():
    """
    Test the check_duplicates function
    """
    assert check_duplicates(df) == 0

def check_missing_values(df):
    """
    Check the number of missing values in the dataset
    """
    return df.isnull().sum().sum()

def test_check_missing_values():
    """
    Test the check_missing_values function
    """
    assert check_missing_values(df) == 0

def check_max_values(df):
    max_values = df.max()
    assert all(max_values <= 100)  # Проверяем, что все максимальные значения не превышают 100

def test_check_max_values():
    check_max_values(df)

def check_min_values(df):
    min_values = df.min()
    assert all(min_values >= 0)  # Проверяем, что все минимальные значения больше или равны 0

def test_check_min_values():
    check_min_values(df)

def check_data_types(df):
    assert df.dtypes.all()  # Проверяем, что все столбцы имеют одинаковый тип данных

def test_check_data_types():
    check_data_types(df)
