import pandas as pf
import glob

csv_list=glob.glob('*.csv')

print('Processing %s csv files'%len(csv_list))

for i in csv_list:
    fr=open(i,'rb').read()
    with open('ENDFILE.csv','ab') as f:
        f.write(fr)

print('Done......')
