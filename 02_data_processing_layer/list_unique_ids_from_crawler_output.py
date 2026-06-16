import pandas as pd
import os

""" this script counts list of unique id accross csv files in multiple folder produced by scraper
"""

ids =[]
all_csvs=[]
for root, directories, files in os.walk("./", topdown=False):
    for name in files:
        f=(os.path.join(root, name))
        if f.endswith(("metadata.csv")):
            all_csvs.append(f)
# iterate thorugh each csv file and build list of universal keys out of it
for csv_file in all_csvs:
    flag=False
    try:
        df=pd.read_csv(csv_file)
        flag=True
    except:
        pass
    if flag:
        for id in list(df['prod_id']):
            ids.append(id)


print(len(ids))
print(len(set(ids)))