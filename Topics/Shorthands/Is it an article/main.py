import re

word = input()
pattern = '^the$'

if re.match(pattern, word):
    print("True")
else:
    print("False")
