import pandas as pd
import numpy as np

df = pd.read_csv("renewable-energy-stock-account-2007-2021.csv")

print(df.info())
print(df.sample(10))
print(df.query(("data_value" > 100000.00) and ('resource == "Solar"')))