
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]
print("my_list[::-1] = ", my_list[::-1])
print("my_list[2:-1:2] = ", my_list[2:-1:2])
print("my_list[6:3:-1] = ", my_list[6:3:-1])

sample_url = 'http://coreyms.com'
print("sample_url = ", sample_url)

# Reverse the url
# print sample_url[::-1]

# # Get the top level domain
# print sample_url[-4:]

# # Print the url without the http://
# print sample_url[7:]

# # Print the url without the http:// or the top level domain
print("sample_url[7:-4] = ", sample_url[7:-4])
