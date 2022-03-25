from nltk.tokenize import regexp_tokenize

sentence = input()

output = regexp_tokenize(sentence, "[A-z'-]+")
print(output)
