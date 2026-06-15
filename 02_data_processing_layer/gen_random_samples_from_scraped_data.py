import os
import shutil
import random

import argparse


'''
After crawling images from ebay, we need to generate subset of images,
which can be used for annotation as well as for training of models
We need a method which should copy n number of images from each attribute value folder
to saparate target folder (that folder will serve as source to annotation and training pipeline) 
'''


'''
gen_random_n_images_samples_dataset()

This method (defined below) will generate dataset containing randomly chosen n number of images from each
attribute value folder

parameters:
n_images # number of images to be chosen from each folder   , default value:500
output_folder='random_images' # name of new destination folder where these random chose images will be copied to 
'''



def gen_random_n_images_samples_dataset(n_images=500,output_folder='random_images'):
    source_folder='./'
    cwd = os.getcwd().split('/')[-1]
    attributes_folders=[name for name in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, name)) and '.ipynb' not in name ]
    print(attributes_folders)
    n_images = n_images
    # iterate through each attributes parent folder
    for attribute in attributes_folders:
        print('processing ',attribute)
        # get attrib_vals folder for each attribute folder
        _, attrib_vals,files = next(os.walk(attribute))
        # get iamges from each attribute val folder
        for attrib_val in attrib_vals:
            print('processing ',attrib_val)
            attrib_val_img_paths=[]    #list of paths of images residing in one folder
            for root,directories, files in os.walk('./'+attribute+'/'+attrib_val+'/'):
                for name in files:
                    f=(os.path.join(root,name))
                    if f.endswith((".png","jpeg","jpg")):
                        attrib_val_img_paths.append(f)
            random_imgs=random.sample(attrib_val_img_paths,min(len(attrib_val_img_paths),n_images))

            # now create other directory and copy images to there
            target_folder='../'+output_folder+'/'
            target_dir = target_folder+str(attribute)+'/'+str(attrib_val)+'/'            
            if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
            for path in random_imgs:
                src_img=path
                dest_img=path[2:]
                dest_img = dest_img.replace("/","--")
                dest_img = cwd+'_'+dest_img
                shutil.copy(src_img,target_dir+dest_img)
                print('copied '+dest_img+' to '+str(target_dir))


gen_random_n_images_samples_dataset(n_images=350,output_folder="random_hoodies_350")


