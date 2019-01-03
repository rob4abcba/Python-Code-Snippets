
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print("student = ", student)
print("student['name'] = ", student['name'])
print("student['courses'] = ", student['courses'])
print("student.get('name') = ", student.get('name'))
print("student.get('courses') = ", student.get('courses'))
print("student.get('phone') = ", student.get('phone'))
print("student.get('phone', 'Not Found') = ", student.get('phone', 'Not Found'))
student['phone'] = '555-1212'
print("student.get('phone', 'Not Found') = ", student.get('phone', 'Not Found'))
student['name'] = 'JANE'
print("student = ", student)
student.update({'name': 'Frank', 'age': 58, 'cell': '123-5555'})
print("student = ", student)
del student['courses']
print("student = ", student)
age = student.pop('age')
print("student = ", student)
print("age = ", age)
print("len(student) = ", len(student))
print("student.keys() = ", student.keys())
print("student.values() = ", student.values())
print("student.items() = ", student.items())

for key in student:
    print("key = ", key)
for key, value in student.items():
    print("key, value = ", key, value)
