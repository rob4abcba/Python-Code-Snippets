print("import my_module")
import my_module
courses = ['History', 'Math', 'Physics', 'CompSci']
index = my_module.find_index(courses, 'Math')
print("index = my_module.find_index(courses, 'Math') = ", index)

print("\nimport my_module as mm")
import my_module as mm
courses = ['History', 'Math', 'Physics', 'CompSci']
index = mm.find_index(courses, 'Math')
print("index = mm.find_index(courses, 'Math') = ", index)

print("\nfrom my_module import find_index")
from my_module import find_index, test
courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print("index = find_index(courses, 'Math') = ", index)
print("test = ", test)

print("\nfrom my_module import find_index as fi, test")
from my_module import find_index as fi, test
courses = ['History', 'Math', 'Physics', 'CompSci']
index = fi(courses, 'Math')
print("index = fi(courses, 'Math') = ", index)
print("test = ", test)

import sys
sys.path.append('/Desktop')
#sys.path.append("C:\Users\rob_t")
print("\nsys.path = ", sys.path)

import random
random_course = random.choice(courses)
print("\nrandom_course = ", random_course)

import math
rads = math.radians(90)
print("rads = math.radians(90) = ", rads)
print("math.sin(rads) = ", math.sin(rads))

import datetime
import calendar
today = datetime.date.today()
print("\ntoday = datetime.date.today() = ", today)
print("calendar.isleap(2020) = ", calendar.isleap(2020))

import os
print("os.getcwd() = ", os.getcwd())
print("os.__file__ = ", os.__file__)

