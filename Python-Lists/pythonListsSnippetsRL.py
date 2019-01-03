# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print("list_1 = ", list_1)
print("list_2 = ", list_2)
list_1[0] = 'Herstory'
print("After list_1[0] = 'Herstory':")
print("list_1 = ", list_1)
print("list_2 = ", list_2)
print("Notice that any time you change list_1, then list_2 automatically changes to follow it.")
print("because they are both the same mutable object.")
print("len(list_1) = ", len(list_1))
print("list_1[0] = ", list_1[0])
print("list_1[-1] = ", list_1[-1])
print("list_1[0:2] = ", list_1[0:2])
print("list_1[:2] = ", list_1[:2])
print("list_1[2:] = ", list_1[2:])
list_1.append('Art')
print("After list_1.append('Art'), then list_1 = ", list_1)
list_1.insert(0, 'Cooking')
print("After list_1.insert(0, 'Cooking'), then list_1 = ", list_1)
extra = ['Track', 'Field']
list_1.insert(1, extra)
print("After list_1.insert(1, extra), then list_1 = ", list_1)
list_1.extend(extra)
print("After list_1.extend(extra), then list_1 = ", list_1)
list_1.remove(extra)
print("After list_1.remove(extra), then list_1 = ", list_1)
list_1.remove('Track')
print("After list_1.remove('Track'), then list_1 = ", list_1)
popped1 = list_1.pop()
print("After list_1.pop(), then list_1 = ", list_1)
print("popped1 = list_1.pop() = ", popped1)
popped2 = list_1.pop()
print("After another list_1.pop(), then list_1 = ", list_1)
print("popped2 = another list_1.pop() = ", popped2)
list_1.reverse()
print("After list_1.reverse(), then list_1 = ", list_1)
list_1.sort() #Methods like this alter the original list_1 in place
print("After list_1.sort(), then list_1 = ", list_1)
nums = [1,5,2,4,3]
print("nums = ", nums)
nums.sort()
print("After nums.sort(), then nums = ", nums)
list_1.sort(reverse=True)
print("After list_1.sort(reverse=True), then list_1 = ", list_1)
nums.sort(reverse=True)
print("After nums.sort(reverse=True), then nums = ", nums)

sorted_list_1_baby = sorted(list_1) #To get sorted version without affecting original list_1
print("sorted_list_1_baby = sorted(list_1) = ", sorted_list_1_baby)
print("original list_1 is untouched thus still = ", list_1)
print("list_1.index('Math') = ", list_1.index('Math'))
print("Boolean 'Math' in list_1 = ", 'Math' in list_1)
print("Boolean 'Art' in list_1 = ", 'Art' in list_1)

for item in list_1:
	print("item = ", item)
for item in enumerate(list_1):
	print("enumerate item = ", item)
for index, item in enumerate(list_1):
	print("index, item = ", index, item)
for index, item in enumerate(list_1, start=1):
	print("If start=1: index, item = ", index, item)

list_1_joined = ', '.join(list_1)
print("list_1_joined = ', '.join(list_1) = ", list_1_joined)
list_1_joined = ' - '.join(list_1)
print("list_1_joined = ' - '.join(list_1) = ", list_1_joined)
new_list = list_1_joined.split(' - ')
print("new_list = list_1_joined.split(' - ') = ", new_list)

print("min(nums) = ", min(nums))
print("max(nums) = ", max(nums))
print(" original nums unchanged = ", nums)
print("nums.index(4) = ", nums.index(4))
print("sum(nums) = ", sum(nums))


# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print("tuple_1 = ", tuple_1)
print("tuple_2 = ", tuple_2)
# tuple_1[0] = 'Art'  #CANNOT do this since tuples are IMMUTABLE


# Sets
python_set = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print("Python sets associate items together without caring about order plus removes duplicates.")
print("python_set = ", python_set)
print("Notice that each time you run, the order changes randomly, plus python automatically removes the duplicate 'Math' item.")
print("len(python_set) = ", len(python_set))
print("We can do membership tests in both lists and sets as shown below:")
print("Boolean 'Math' in list_1 = ", 'Math' in list_1)
print("Boolean 'Math' in python_set = ", 'Math' in python_set)
print("However, since sets automatically remove duplicates, sets are optimized for membership tests.")
#print("python_set[0] = ", python_set[0]) #TypeError: 'set' object does not support indexing
set1 = {'History', 'Math', 'Physics', 'CompSci'}
set2 = {'History', 'Math', 'Art', 'Design'}
print("set1 = ", set1)
print("set2 = ", set2)
print("set1.intersection(set2) = ", set1.intersection(set2))
print("set1.union(set2) = ", set1.union(set2))
print("set1.difference(set2) = ", set1.difference(set2))
print("set2.difference(set1) = ", set2.difference(set1))


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()
