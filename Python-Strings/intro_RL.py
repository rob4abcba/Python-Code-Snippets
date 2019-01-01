message = '''There are many questions homeowners ask themselves during the selling process. 
"How much will my home sell for?"  "How much should I list my home for?"  
"Who should I select as a real estate agent to sell my home?"  "What if the real 
estate agent overprices my home?"  Last but not least, "Is this a good time to be 
selling a home?" is also a very common question that real estate agents are asked.'''

print(message)
print(len(message))
print(message.count("real estate"))
print(message.find("real estate"))
new_message = message.replace("real estate", "fake estate")
print(new_message)

print(message[3:9])
print(len(message[3:9]))

print(message[0:9])
print(len(message[0:9]))
print(message[0:9].lower())

message = message.replace("the", "da")
print(message)

greeting = 'Hello'
name = 'Michael'
message = "{} .... {}!!  You da man!".format(greeting, name)
print(message)
message = f"Really {greeting} .... {name}!!  You da man!"
print(message)
message = f"{greeting.upper()} .... {name.upper()}!!  You da man!"
print(message)

print(dir(message))
#print(help(str))
print(help(str.lower))

