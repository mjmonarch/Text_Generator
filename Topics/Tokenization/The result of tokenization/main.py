import nltk

text = input()
sentences = nltk.tokenize.sent_tokenize(text)

print(sentences)
