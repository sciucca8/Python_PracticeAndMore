import numpy as np
import pandas as pd

db = pd.read_csv('googleplaystore.csv')

db = db.drop(columns=["Current Ver","Android Ver"])

print(db.columns)