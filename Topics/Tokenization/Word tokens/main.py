# import nltk
# nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = input()

words = word_tokenize(text)
print(words)
