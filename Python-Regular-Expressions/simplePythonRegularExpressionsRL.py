import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

'''

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
for match in matches:
	print("match(r'abc') = ", match)

pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)
for match in matches:
	print("match(r'\.') = ", match)

pattern = re.compile(r'\W')
matches = pattern.finditer(text_to_search)
for match in matches:
	print("match(r'\W') = ", match)

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
	print("match(r'\d\d\d.\d\d\d.\d\d\d\d') = ", match)

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
	print("match(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') = ", match)

pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
matches = pattern.finditer(text_to_search)
for match in matches:
	print("match(r'\d{3}[-.]\d{3}[-.]\d{4}') = ", match)

pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
	print("match(r'[89]00[-.]\d\d\d[-.]\d\d\d\d') = ", match)

print("\nwith open('data.txt', 'r', encoding='utf-8') as f:")
with open('data.txt', 'r', encoding='utf-8') as f:
	contents = f.read()
	matches = pattern.finditer(contents)
	for match in matches:
		print("match(r'[89]00[-.]\d\d\d[-.]\d\d\d\d') = ", match)

pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search)
for match in matches:
	print("match(r'[^b]at') = ", match)


pattern = re.compile(r'coreyms\.com')
matches = pattern.finditer(text_to_search)
for match in matches:
	print("match(r'coreyms\.com') = ", match)

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
	print("match(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') = ", match)

sentence = 'Start a sentence and then bring it to an end'



pattern = re.compile(r'start', re.I)

matches = pattern.search(sentence)

print(matches)
