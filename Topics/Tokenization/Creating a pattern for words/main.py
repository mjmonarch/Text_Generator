from nltk.tokenize import regexp_tokenize

text = input()
num = int(input())

words = regexp_tokenize(text, "[a-zA-Z]+")

print(words[num])