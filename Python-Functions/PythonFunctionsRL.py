def hello_func():
    pass
print("hello_func = ", hello_func)
print("hello_func() = ", hello_func())
hello_func() #RL This does nothing and prints nothing.

def run_func():
    print("Run this Function !!")
print("run_func = ", run_func)
print("run_func() = ", run_func()) #RL Executes function before executing the print operation.
run_func()

def return_func():
    return "Return this Function !!"
print("return_func = ", return_func)
print("return_func() = ", return_func()) #RL Executes function before executing the print operation.
return_func() #RL Doesnt show us anything without print statement to show it.
print("return_func().upper() = ", return_func().upper())

def greeting_func(greeting):
    return '{} Function'.format(greeting)
Yo = "Hey"
print("greeting_func(Yo) = ", greeting_func(Yo))

def greeting2_func(greeting, name='You'):
    return '{} {}'.format(greeting, name)
Yo = "Heyyyy"
print("greeting2_func(Yo) = ", greeting2_func(Yo))

def greeting2_func(greeting, name='You'):
    return '{} {}'.format(greeting, name)
print("greeting2_func('Hi','Fred') = ", greeting2_func('Hi','Fred'))

def student_info(*args, **kwargs):
    print("args = ", args)
    print("kwargs = ", kwargs)
student_info('Math', 'Music', name='John', age=22)

courses = ('Math', 'Music')
info = {'name': 'John', 'age': 22}
student_info(courses, info)

student_info(*courses, **info)


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print("is_leap(2017) = ", is_leap(2017))
print("is_leap(2020) = ", is_leap(2020))

def days_in_month(year, month):
    """Return number of days in that month in that year."""
    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
print("days_in_month(2017, 2) = ", days_in_month(2017, 2))
print("days_in_month(2020, 2) = ", days_in_month(2020, 2))

