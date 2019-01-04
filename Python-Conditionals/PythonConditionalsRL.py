language = 'JavaScript'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
	print('Language is Java')
elif language == 'JavaScript':
	print('Language is JavaScript')
else:
    print('No match')

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Need BOTH Admin AND logged_in')

if user == 'Admin' or logged_in:
	print('Admin Page')
else:
	print('Need Admin OR logged_in')

if not logged_in:
	print('Please Log In')
else:
	print('You are logged in.  Welcome.')

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

a = [1,2,3]
b = [1,2,3]
print("a == b?", a == b)
print("a is b?", a is b)
print("id(a)?", id(a))
print("id(b)?", id(b))
b = a
print("a == b?", a == b)
print("a is b?", a is b)
print("id(a)?", id(a))
print("id(b)?", id(b))


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False
print('False:')
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = None
print('None:')
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0
print('0:')
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 7
print('7:')
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = ''
print("'':")
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 'Joe'
print("'Joe':")
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


condition = ()
print("():")
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = ('Joe')
print("('Joe'):")
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


condition = []
print("[]:")
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = ['Joe']
print("['Joe']:")
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


condition = {}
print('{}:')
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = {"Joe"}
print("{'Joe'}:")
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')



