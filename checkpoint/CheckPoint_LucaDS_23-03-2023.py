import pandas as pd
import numpy as np

"""Lower Bound: (Q1 - 1.5 * IQR)
Upper Bound: (Q3 + 1.5 * IQR)"""

df = pd.read_csv("train.csv")
print(df.columns)
print(df.dtypes[df.dtypes != object])
col_num = df.loc[:, df.dtypes != object].columns.to_list()
for column in col_num:
    q1, q3 = np.percentile(df[column], [25,75])
    interq = q3 - q1 
    my_count = df[column] < (q1 - 1.5 * interq)
    my_count2 = df[column] > (q3 + 1.5 * interq)
    x = my_count.sum()
    y = my_count2.sum()

    print(x + y)
    





