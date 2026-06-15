import os
import random as rand
import shutil
import argparse

'''
parameters
'''
extension = '.jpg'
number = 10
source_dir = './source_directory'
dest_dir = './dest_directory'
is_rand = 'yes'
all_files = 'no'

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--number', type=int, default=number)# Parse the argument

parser.add_argument('--ext', type=str, default=extension)# Parse the argument
parser.add_argument('--src_dir', type=str, default=source_dir)# Parse the argument
parser.add_argument('--dest_dir', type=str, default=dest_dir)# Parse the argument
parser.add_argument('--rand', type=str, default=is_rand)# Parse the argument
parser.add_argument('--all_files', type=str, default=all_files)# Parse the argument


args = parser.parse_args() # get arguments variable


'''
walk through directory and get paths of images
'''
images = []
for root, dirs, files in os.walk(args.src_dir):
    for file in files:
        if file.endswith(args.ext):
            images.append(os.path.join(root,file))


'''
check if images selection mode is random
'''
if args.all_files=='yes':
    final_images=images
elif args.rand=='yes':
    final_images=rand.sample(images,args.number)
else:
    final_images = images[:args.number]


'''
copy all files from source to destinition folder
'''
copied_count = 0
for img in final_images:
    if os.path.exists(os.path.join(args.dest_dir,img.split('/')[-1])):
        print(f'{img} skipped, allready exists')
    else:
        shutil.copy(img, args.dest_dir)
        print(f'{img} >>> {args.dest_dir}')
        copied_count+=1
print(f'{copied_count} files copied')
