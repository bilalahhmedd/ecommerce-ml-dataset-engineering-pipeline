import os
from shutil import copy
dir_src = r"../random_women_tops_350"
dir_dst = r"../flattened_scraped_images"
for root, _, files in os.walk(dir_src):
    for file in files:
        if file.endswith('.jpg'):
            copy(os.path.join(root, file), dir_dst)


