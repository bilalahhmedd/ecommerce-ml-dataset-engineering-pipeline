import pandas as pd
import os
import shutil
'''
copy sample images from source folder to destination folder
'''


source_dir = './hoodies-remaining/'
target_dir = './hoodies-jackets-visual-samples/hoodies-remaining/'


attributes = os.listdir(source_dir)

for i in attributes:
    attrib_vals=os.listdir(source_dir+i)
    print(attrib_vals)
    for j in attrib_vals:
        try:
            counter=0
            for root,_,files in os.walk(source_dir+i+'/'+j,topdown=False):
                print(root,files)
                path_string = root.split('.')[1].split('/')
                if not os.path.exists(target_dir+path_string[2]+'/'+path_string[3]+'/'):
                    os.makedirs(target_dir+path_string[2]+'/'+path_string[3]+'/')
                    print('driectory created successfully')
                for file in files[:3]:
                    if file.endswith('.jpg'):
                        shutil.copy(root+'/'+file,target_dir+path_string[2]+'/'+path_string[3]+'/'+str(counter)+'_'+file)
                        print(file,' copied')
                print('files copied successfully')
                counter+=1
                if counter >= 34:
                    break
        except Exception as e:
            print('Exception accured')
            pass


