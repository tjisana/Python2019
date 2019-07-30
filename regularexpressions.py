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
sentence = 'Start a sentence and then bring it to an end'
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'M[rs]+\.?\s[A-Z]\w*')

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
for match in pattern.finditer(urls):
    print(match.group(3))