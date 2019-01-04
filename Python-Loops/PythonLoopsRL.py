nums = [11,3,8]

for num in nums:
	print("num = ", num)

for num in nums:
	if num == 3:
		print('Found 3 !!')
		continue #RL Continue for loop, but skip print statement below.
	print("num = ", num)

for num in nums:
	for letter in 'abc':
		print("num, letter = ", num, letter)

for i in range(3):
	print("i = ", i)
	print("num = ", num)

for i in range(12,15):
	print("i = ", i)
	print("nums = ", nums)

ind = 0
while ind < 3:
    print("ind = ", ind)
    ind += 1

x = 0
while True: #RL True instead of conditional creates infinite loop that need to break out of.
    if x == 5:
         break #RL If never hit this break, then need Ctrl + C to stop infinite loop.
    print("x = ", x)
    x += 1



# x = 0

# while True:
#     # if x == 5:
#     #     break
#     print(x)
#     x += 1
