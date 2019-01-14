#!/usr/bin/python

#RL Python 3.4 introduced a new standard library for dealing with files and paths called pathlib
from pathlib import Path

#RL pass a path or filename into a new Path() object using forward slashes and it handles the rest:
#data_folder = Path("source_data/text_files/")
data_folder = Path("/c/Users/rob_t/Videos/WinX YouTube Downloader/Automate the Boring Stuff with Python/")
data_folder = Path("/c/Users/rob_t/Videos/")
data_folder = Path("C:/Users/rob_t/Videos/")
data_folder = Path("/Users/rob_t/Videos/")


import os

# Am I in the correct directory?
print('os.getcwd() = ', os.getcwd())
#print('dir(os) = ', dir(os))

file_to_open = data_folder / "raw_data.txt"
#file_to_open = data_folder / "Lesson 1 - Python Programming (Automate the Boring Stuff with Python).mp4"

#f = open(file_to_open)

#print(f.read())

#import os
path = "/usr/tmp"
path = "/Users/rob_t/Videos/"
path = "/Users/rob_t/Videos/4K Video Downloader/"

# # Check current working directory.
# retval = os.getcwd()
# print("Current working directory %s" % retval)

# Now change the directory
os.chdir( path )
print('os.getcwd() = ', os.getcwd())

os.chdir(data_folder)
print('os.getcwd() = ', os.getcwd())

# # Check current working directory.
# retval = os.getcwd()

# print("Directory changed successfully %s" % retval)


# print('os.chdir(specify path here)')
# #os.chdir("C\:\\Users\rob_t\Videos\WinX YouTube Downloader\Automate the Boring Stuff with Python")
# #os.chdir('.')
# os.chdir('C:')

# # Am I in the correct directory?
# print('os.getcwd() = ', os.getcwd())

# print('dir(os) = ', dir(os))

# Print all the current file names
for f in os.listdir():
    # If .DS_Store file is created, ignore it
    if f == '.DS_Store':
        continue

    file_name, file_ext = os.path.splitext(f)
    print(file_name)

#     # One way to do this
#     f_title, f_course, f_number = file_name.split('-')

#     # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

#     # Need to remove whitespace
#     f_title = f_title.strip()
#     f_course = f_course.strip()
#     # f_number = f_number.strip()

#     # Want to remove the number sign?
#     # f_number = f_number.strip()[1:]

#     # One thing I noticed about this output is that if it was sorted by filename
#     # then the 1 and 10 would be next to each other. How do we fix this? One way we can fix this is to pad
#     # the numbers. So instead of 1, we'll make it 01. If we had hundreds of files then this would maybe need to be 001.
#     # We can do this in Python with zfill
#     f_number = f_number.strip()[1:].zfill(2)

#     # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

#     # You have the power to reformat in any way you see fit
#     print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

#     new_name = '{}-{}{}'.format(file_num, file_title, file_ext)

#     os.rename(fn, new_name)


# # print(len(os.listdir()))
