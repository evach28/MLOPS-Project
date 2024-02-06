import os
import pandas as pd
from fetch_data import fetch_data

def test_fetch_data():
    filepath = os.path.join(os.getcwd(), 'dataset', 'transfusion.data')
    data = fetch_data(filepath)
    assert not data.empty
    assert isinstance(data, pd.DataFrame)
    print("First 5 rows :")
    print(data.head(5))