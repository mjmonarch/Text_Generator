import re

pattern = '[B-N][aeoiuy]'

name = input()
if re.match(pattern, name):
    print("Suitable!")
