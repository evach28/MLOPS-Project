import pandas as pd

def fetch_data(filepath):
    data = pd.read_csv(filepath, header=",")
    return data