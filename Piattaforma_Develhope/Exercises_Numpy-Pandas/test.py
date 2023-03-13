# Group companies by first letter(lower) and take the mean incidents_85_99 and make it a dataframe again 
import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv("airline_safety_data.txt")
dct = {}

df["firstletter"] = df.airline.str[0].str.lower()

first_letter_mean = pd.DataFrame(df.groupby(["firstletter"])["incidents_85_99"].mean())
print(first_letter_mean)



