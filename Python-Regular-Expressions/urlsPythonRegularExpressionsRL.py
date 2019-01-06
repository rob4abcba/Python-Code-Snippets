import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

#pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

# for match in matches:
#     print("match.group(0) = ", match.group(0))

# for match in matches:
#     print("match.group(1) = ", match.group(1))

# for match in matches:
#     print("match.group(2) = ", match.group(2))

subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

matches = pattern.finditer(urls)

# for match in matches:
#     print("match.group(0) = ", match.group(0))

# for match in matches:
#     print("match.group(1) = ", match.group(1))