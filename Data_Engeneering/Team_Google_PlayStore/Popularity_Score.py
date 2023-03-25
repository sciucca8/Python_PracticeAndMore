"""1) Popularity score = Rating * Installs / 1_000_000 ---- nome app
2) top/bottom n Apps by Popularity ---- top/bottom, n, only name/whole line
3) top/bottom free/paid n Apps by popularity
4) top/bottom n Categories by popularity"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Literal

df = pd.read_csv("GooglePS.csv")
df.corr()
print(df.loc[df["Installs"] == 0])
df["Popularity"] = round(df.Installs * df.Rating / 1_000_000, 4)

print(df.Popularity.value_counts().sort_index())
#print(df.loc[df["Popularity"] == 0].count())

def popularity_score(n= 10, ascend= False, all_info= False, free= "all",):
    if free != "all":
        if free == True:
            df_popularity = df[df["Type"] == "Free"].sort_values(by= ["Popularity", "Installs", "Rating"], ascending= [ascend, ascend, ascend])[df.columns if all_info else ["App"]].head(n)
        else:
            df_popularity = df[df["Type"] == "Paid"].sort_values(by= ["Popularity", "Installs", "Rating"], ascending= [ascend, ascend, ascend])[df.columns if all_info else ["App", "Popularity"]].head(n)
    else:
        df_popularity = df.sort_values(by= ["Popularity", "Installs", "Rating"], ascending= [ascend, ascend, ascend])[df.columns if all_info else ["App"]].head(n)

    plt.bar(df_popularity["App"], df_popularity["Popularity"])
    plt.xticks(rotation= "vertical")
    plt.show()
    return df_popularity, plt

ps, ps_graph = popularity_score(20, False, False, False)
print(ps)
ps_graph.show()

