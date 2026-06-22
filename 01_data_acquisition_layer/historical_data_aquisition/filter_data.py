'''
This script filters out products
based on keywords you pass
and builds csv file contianing products id with images ids
That csv file will be fed to get_data.py module to download images
'''

import pandas as pd
import csv
import os
from collections import Counter
#import openpyxl
import re
import json


#from pandas_multiprocess import multi_process
from pathlib import Path
import wget


# keyword you search for 
keyword = 'top'

# read csv file
products_df= pd.read_csv('./input/products.csv')


# process data and get 
imp_col=['productString','title','category','shortDescription','keywords']
prod_ids = []
image_ids = []
data=[]
counter=0
print(f'processing')
for product in products_df['products']:
    for prod in json.loads(product):
        tmp_keys = prod.keys()
        fnl_cols = set(imp_col).intersection(set(tmp_keys))
        fnl_cols = list(fnl_cols)
        string_ =''
        for i in fnl_cols:
            string_ = string_+str(prod[i])
        string_ = string_.lower().replace('%20',' ').replace('%0a',' ').replace('%3a',' ')
        try:
            if keyword in string_ and ('women' in string_ or 'woman'in string_) and ('shoe' not in string_ and 'sneaker' not in string_):
                
                #prod_ids.append(prod['_id']['$oid'])
                #print('done')
                images = prod['images']
                fnl_imgs = [v for k,v in images.items()]
                #image_ids.append(fnl_imgs)
                data.append({'prod_id':prod['_id']['$oid'],'images':fnl_imgs,'string':string_})
                counter+=1
                
        except:
            #print('skipped')
            pass
            
print(f'{counter} products found')

output_df=pd.DataFrame(data)

output_df.to_csv(f'./output/csv/latest_women_{keyword}_to_get.csv')
print(f'women_{keyword}_to_get generated successfully')
