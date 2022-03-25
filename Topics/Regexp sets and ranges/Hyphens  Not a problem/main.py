import re

template = '[a-z]*-[a-z]*'
word = input()

if re.match(template, word):
    print("True")
else:
    print("False")
