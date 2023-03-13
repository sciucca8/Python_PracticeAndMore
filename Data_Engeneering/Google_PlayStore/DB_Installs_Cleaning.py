import pandas as pd
import numpy as np

df = pd.read_csv("googleplaystore.csv")

#print(np.where(df.Installs == "0+"))
#print(df.loc[[4465, 5307, 5486, 5945, 6692, 7434, 8081, 8614, 8871, 9337, 9719, 9905, 9917, 9934], ["Installs"]])

def correction_row_10472(df):
    col_ls = list(df.columns)
    row_10472 = np.where(df.Size == "1,000+")[0][0]
    
    for i in range(len(col_ls[2:])):

        df[col_ls[len(col_ls) - (i + 1)]][row_10472] = df[col_ls[len(col_ls) - (i + 2)]][row_10472]

    df.Category[10472] = "Lifestyle"
    return df

df = correction_row_10472(df)

"""for i in range(len(df.Installs)):
    print(list(df.Installs[i]))"""

def Installs_Cleaning(df):

    for i in range(len(df)):
        if df.Installs[i] == "0+":
            df.Installs[i] = "1"
        if "," in df.Installs[i]:
            df.Installs[i] = "".join(list(x for x in df.Installs[i][:len(df.Installs[i]) -1] if x != ","))
        if "+" in df.Installs[i]:
            df.Installs[i] = df.Installs[i][:len(df.Installs[i]) -1]

    
    """for i in range(len(df.Installs)):
        ls = list(reversed(df.Installs[i]))             #Aggiungo un punto ogni terzo numero cosi da rendere piu leggibile il numero
        for m in range(len(ls)):                        #Ma con i punti il numor non e transformabile in int
            if m % 3 == 0 and m != 0:
                ls[m] += ","""

    df["Installs"] = df.Installs.astype(int)
    return df

    

df = Installs_Cleaning(df)

print(df.Installs.sample())


