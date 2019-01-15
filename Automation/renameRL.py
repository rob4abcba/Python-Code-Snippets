#!/usr/bin/python

import os
#print('dir(os) = ', dir(os)) #Shows all available methods in os module. See that getcwd is one of them.
print('Initially, os.getcwd() = ', os.getcwd()) #cwd = current working directory

#path1 = "/usr/tmp"
path1 = "/Users/rob_t/Videos/WinX YouTube Downloader/"
os.chdir( path1 ) #change directory
print('After os.chdir( path1 ), os.getcwd() = ', os.getcwd())

#Python 3.4 introduced pathlib (a new standard library for dealing with files and paths)
from pathlib import Path

#Pass a path or filename into a new Path() object using forward slashes and pathlib handles the rest:
path2 = Path("/c/Users/rob_t/Videos/WinX YouTube Downloader/Automate the Boring Stuff with Python/")
path2 = Path("C:/Users/rob_t/Videos/WinX YouTube Downloader/Automate the Boring Stuff with Python/")
path2 = Path("/Users/rob_t/Videos/WinX YouTube Downloader/Automate the Boring Stuff with Python/")
os.chdir(path2)
print('After pathlib, os.getcwd() = ', os.getcwd())

file_to_open = path2 / "raw_data.txt"
#file_to_open = path2 / "Lesson 1 - Python Programming (Automate the Boring Stuff with Python).mp4"

#f = open(file_to_open)

#print(f.read())

# # Check current working directory.
# retval = os.getcwd()
# print("Current working directory %s" % retval)

# print("Directory changed successfully %s" % retval)

# Print all the current file names
for f in os.listdir():
    # If .DS_Store file is created, ignore it
    if f == '.DS_Store':
        continue
    print("\nos.path.splitext(f) = ", os.path.splitext(f))
    f_name, f_ext = os.path.splitext(f)
    print("f_name = ", f_name, "\tf_ext = ", f_ext)
    f_name = f_name.strip()
    f_ext = f_ext.strip()

    print("\nf_name.split('-') = ", f_name.split('-'))
    f_lesson, f_course = f_name.split('-')
    print("f_lesson = ", f_lesson, "\tf_course = ", f_course)
    f_lesson = f_lesson.strip()
    f_course = f_course.strip()

    print("\nf_lesson.split(' ') = ", f_lesson.split(' '))
    f_Lesson, f_num = f_lesson.split(' ')

    print("f_Lesson = ", f_Lesson, "\tf_num = ", f_num)

    print('{}-{}{}'.format(f_num, f_course, f_ext))

    # Need to remove whitespace
    f_num = f_num.strip() #Strip off whitespace from beg and end
    f_course = f_course.strip()
    print("Before zfill(2), f_num = ", f_num)
    # f_number = f_number.strip()

    # Want to remove the number sign?
    # f_number = f_number.strip()[1:]

    # If sorted by filename, then the order 
    # would be 1, 11, 12, ... 2, 3, ... 
    # instead of 1, 2, 3, ... 9, 10, 11
    # Pad numbers, so instead of 1, format them like 01 using zfill(2) 
    # If hundreds of files, then format them like 001 using zfill(3)
    f_num = f_num.zfill(2)
    print("After  zfill(2), f_num = ", f_num)

    print('{}-{}{}'.format(f_num, f_course, f_ext))
    new_name = '{}-{}{}'.format(f_num, f_course, f_ext)

    os.rename(f, new_name)


# # print(len(os.listdir()))
