import pandas as pd                     
import numpy as np   

db = pd.read_csv('googleplaystore.csv')

db.loc(10472, ["Rating"])
