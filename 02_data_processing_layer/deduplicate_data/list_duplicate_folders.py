import os

""" 
a utility script to print duplicate folders in terminal output
"""
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