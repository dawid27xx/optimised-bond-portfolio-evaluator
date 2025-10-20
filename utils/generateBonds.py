import pandas as pd
from datetime import date
from models.bond import Bond

def loadBonds(path):
    df = pd.read_csv(path, parse_dates=["issueDate", "maturityDate"])
    bonds = []

    for _, row in df.iterrows():
        bond = Bond(
            face=float(row["face"]),
            couponRate=float(row["couponRate"]),
            maturityDate=row["maturityDate"].date(),
            issueDate=row["issueDate"].date(),
            frequency=int(row["frequency"]),
            dayCount=row["dayCount"]
        )
        bonds.append((row["issuer"], bond))

    return bonds
