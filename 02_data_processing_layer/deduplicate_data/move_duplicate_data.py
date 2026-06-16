import pandas as pd
import os
import numpy as np
from collections import Counter
import shutil

""" util script to move duplicate data to trash folder
"""

def gen_path(duplicate_path):
    """_summary_

    Args:
        duplicate_path (_str_): _folder path containing duplicated images_

    Returns:
        _str_: _temporary path_
        _str_: _folder name_
    """
    folder=duplicate_path.split('/')[-1]
    tmp_pth=''
    for fldr in duplicate_path[2:].split('/')[:-1]:
        tmp_pth=tmp_pth+'/'+fldr
    tmp_pth=tmp_pth+'/'
    return tmp_pth,folder

paths = []
for root, directory, files in os.walk('./',topdown=False):
    paths.append(root)
unique_folders = []
duplicates = []
for path in paths:
    tmp = path.split('/')
    if len(tmp)>=6:
        folder_id = path.split('/')[-1]
        if folder_id in unique_folders:
            duplicates.append(path)
            print(folder_id+' is duplicate')
        else:
            unique_folders.append(folder_id)

'''
move data to trshed_backup folder
'''

target_dir = '../trashed_backup/'
for duplicate in duplicates:
    dup_path,folder=gen_path(duplicate)
    final_dir = target_dir+dup_path
    if not os.path.exists(final_dir):
        os.makedirs(final_dir)
    shutil.move(duplicate,final_dir)