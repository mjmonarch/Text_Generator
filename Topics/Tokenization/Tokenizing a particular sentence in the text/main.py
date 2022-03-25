from nltk.tokenize import regexp_tokenize
from nltk.tokenize import sent_tokenize

text = input()
num = int(input())

sent_list = sent_tokenize(text)
# print(sent_list)
output = regexp_tokenize(sent_list[num], "[A-z']+")

print(output)
