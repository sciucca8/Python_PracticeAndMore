import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
#from GooglePS_CleanDB import df - chiedi a davide per i print in GooglePS_CleanDB

df = pd.read_csv("GooglePS.csv")
pd.set_option("display.max_rows", None)
display(df.Installs)
print(df.info())
df["Performance"] = df["Installs"] * df["Rating"] / 1_000_000


app_performance_df = df[["App", "Performance"]]

app_performance_df = app_performance_df.sort_values(by="Performance", ascending= False).reset_index(drop=True)
print(app_performance_df["Performance"])

plt.figure(figsize=(5, 6))
plt.bar(app_performance_df["App"].head(3), app_performance_df["Performance"].head(3), width= 0.4)
plt.yticks(np.arange(0, app_performance_df["Performance"].max() + 1_000, 500))
plt.show()

