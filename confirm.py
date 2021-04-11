import pandas as pd 
import numpy as np



base='BaseDirectory'

count=0

filepath=base+r'Your Data Files'

df = pd.read_csv(open(filepath, encoding='utf-8'),sep=',').astype('str')


dfs=df.duplicated(subset ='Data Column')

for i,v in dfs.items():
        if dfs[i]==False:
                count=count+1

print(count)

