
import my_module as mm
print("import my_module as mm")
courses = ['History', 'Math', 'Physics', 'CompSci']

#index = my_module.find_index(courses, 'Math')
#print(index)

index = mm.find_index(courses, 'Math')
print(index)


from my_module import find_index

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)