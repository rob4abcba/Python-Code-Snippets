
greeting = 'Hello'
name = 'Michael'
message = "python2: {} .... {}!!  You da man!".format(greeting, name) #Need to use to format for python2.
print(message)
message = f"python3: {greeting} .... {name}!!  You da man!" #Good for RE form letters to multiple people.  Or cover letters to multiple employers.
print(message)
message = f"python3 UPPERCASE: {greeting.upper()} .... {name.upper()}!!  You da man!" #Good for bolding/highlighting key words.
print(message)

greeting = '你好'
name = '哥哥'
message = "python2 Chinese: {} .... {}!!  You da man!".format(greeting, name)
print(message)
message = f"python3 Chinese: {greeting} .... {name}!!  You da man!"
print(message)