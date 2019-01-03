
# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

num = 3
print(num, type(num))
num = 3.14
print(num, type(num))
num = "Joe"
print(num, type(num))
num = True
print(num, type(num))
num = 3 / 2
print("3 / 2 = ",num, type(num))
num = 3 // 2
print("3 // 2 = ",num, type(num))
num = 3 ** 2
print("3 ** 2 = ",num, type(num))
num = 3 % 2
print("3 % 2 = ",num, type(num))

print("abs(-3) = ",abs(-3), type(num))
print("round(3.735) = ",round(3.735),type(num))
print("round(3.735,1) = ",round(3.735,1),type(num))
print("round(3.735,2) = ",round(3.735,2),type(num))

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num_1 = 3
num_2 = 2
print("num_1 = ",num_1,type(num_1))
print("num_2 = ",num_2,type(num_2))
print("num_1 == num_2? ",num_1 == num_2,type(num_1 == num_2))
print("num_1 != num_2? ",num_1 != num_2,type(num_1 != num_2))
print("num_1 > num_2? ",num_1 > num_2,type(num_1 > num_2))
print("num_1 < num_2? ",num_1 < num_2,type(num_1 < num_2))
print("num_1 >= num_2? ",num_1 >= num_2,type(num_1 >= num_2))
print("num_1 <= num_2? ",num_1 <= num_2,type(num_1 <= num_2))

num_1 = '100'
num_2 = '200'
print("num_1 = ",num_1,type(num_1))
print("num_2 = ",num_2,type(num_2))
print("num_1 + num_2 = ",num_1 + num_2,type(num_1 + num_2))
print("int(num_1) + int(num_2) = ",int(num_1) + int(num_2),type(int(num_1) + int(num_2)))