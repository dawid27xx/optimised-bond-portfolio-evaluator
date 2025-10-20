import pandas as pd

def loadData(path):
    df = pd.read_csv(path)
    tenors = df.iloc[:, 0].values
    spotRates = df.iloc[:, 1].values
    return tenors, spotRates
