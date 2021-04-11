import pandas as pd 
import numpy as np


def ad(df):
    return ';'.join(df.values)
        

base='BaseDirectory'

filepath=base+r'Your Data Files'

df = pd.read_csv(open(filepath, encoding='utf-8'),sep=',').astype('str')



df=df.groupby(['Data Column'])['Data Column'].apply(ad)

df=df.reset_index()


df.to_csv(base+'ENDFILE.csv',encoding='utf_8_sig',index=False)
