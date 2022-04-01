# #------------------------------------STAGE 1------------------------------------
# from nltk.tokenize import WhitespaceTokenizer
#
# file_name = input()
# tk = WhitespaceTokenizer()
# with open(file_name, 'r', encoding='utf-8') as reader:
#     tokens = tk.tokenize(reader.read())
#
# print("Corpus statistics")
# print(f"All tokens: {len(tokens)}")
# print(f"Unique tokens: {len(set(tokens))}")
#
# user_input = input()
# while user_input != 'exit':
#     try:
#         num = int(user_input)
#         if abs(num) >= len(tokens):
#             print("Index Error. Please input an integer that is in the range of the corpus.")
#         else:
#             print(tokens[num])
#     except TypeError:
#         print("Type Error: Please input an integer.")
#     except ValueError:
#         print("Value Error: Please input an integer.")
#     user_input = input()

#------------------------------------STAGE 2------------------------------------
# from nltk.tokenize import WhitespaceTokenizer
# from nltk import bigrams
# from nltk import FreqDist
#
# file_name = input()
# tk = WhitespaceTokenizer()
# with open(file_name, 'r', encoding='utf-8') as reader:
#     tokens = tk.tokenize(reader.read())
#     bigrams_list = list(bigrams(tokens))
#     freq = FreqDist(bigrams_list)
#
# print("Number of bigrams:", len(bigrams_list))
#
# user_input = input()
# while user_input != 'exit':
#     try:
#         num = int(user_input)
#         if abs(num) >= len(bigrams_list):
#             print("Index Error. Please input a value that is not greater than the number of all bigrams.")
#         else:
#             head = "{0:<18}".format("Head: " + bigrams_list[num][0])
#             tail = "{0:<18}".format("Tail: " + bigrams_list[num][1])
#             print(head, tail)
#     except TypeError:
#         print("Type Error: Please input an integer.")
#     except ValueError:
#         print("Value Error: Please input an integer.")
#     user_input = input()

# ------------------------------------STAGE 3------------------------------------
# from nltk.tokenize import WhitespaceTokenizer
# from nltk import bigrams
# from collections import Counter
#
# file_name = input()
#
# tk = WhitespaceTokenizer()
# with open(file_name, 'r', encoding='utf-8') as reader:
#     tokens = tk.tokenize(reader.read())
# bigrams_list = list(bigrams(tokens))
#
# bigrams_list_dict = {}
# for bigram in bigrams_list:
#     bigrams_list_dict.setdefault(bigram[0], []).append((bigram[1]))
#
# for bigram_key in bigrams_list_dict.keys():
#     bigrams_list_dict[bigram_key] = Counter(bigrams_list_dict[bigram_key])
#
# user_input = input()
# while user_input != 'exit':
#     print("Head:", user_input)
#     try:
#         for item in bigrams_list_dict[user_input].most_common():
#             tail = "{0:<18}".format("Tail: " + item[0])
#             count = "{0:<18}".format("Count: " + str(item[1]))
#             print(tail, count)
#     except KeyError:
#         print("Key Error : The requested word is not in the model. Please input another word.")
#     print("")
#     user_input = input()

# ------------------------------------STAGE 4------------------------------------
# from nltk.tokenize import WhitespaceTokenizer
# from nltk import bigrams
# from collections import Counter
# import random
#
# file_name = input()
#
# tk = WhitespaceTokenizer()
# with open(file_name, 'r', encoding='utf-8') as reader:
#     tokens = tk.tokenize(reader.read())
# bigrams_list = list(bigrams(tokens))
#
# bigrams_list_dict = {}
# for bigram in bigrams_list:
#     bigrams_list_dict.setdefault(bigram[0], []).append((bigram[1]))
#
# for bigram_key in bigrams_list_dict.keys():
#     bigrams_list_dict[bigram_key] = Counter(bigrams_list_dict[bigram_key])
#
# for _i in range(10):
#     output = ""
#     start_word = random.choice(list(bigrams_list_dict.keys()))
#     output += start_word
#     for _j in range(9):
#         words = [x[0] for x in bigrams_list_dict[start_word].most_common()]
#         frequency = [x[1] for x in bigrams_list_dict[start_word].most_common()]
#         next_word = random.choices(words, frequency)[0]
#         output = output + " " + next_word
#         start_word = next_word
#     print(output)

# #------------------------------------STAGE 5------------------------------------
# from nltk.tokenize import WhitespaceTokenizer
# from nltk import bigrams
# from collections import Counter
# import random
#
# PUNCTUATION_MARKS = ['.', '!', '?']
#
# file_name = input()
#
# tk = WhitespaceTokenizer()
# with open(file_name, 'r', encoding='utf-8') as reader:
#     tokens = tk.tokenize(reader.read())
# bigrams_list = list(bigrams(tokens))
#
# bigrams_list_dict = {}
# for bigram in bigrams_list:
#     bigrams_list_dict.setdefault(bigram[0], []).append((bigram[1]))
#
# for bigram_key in bigrams_list_dict.keys():
#     bigrams_list_dict[bigram_key] = Counter(bigrams_list_dict[bigram_key])
#
# for _i in range(10):
#     output = ""
#     start_word = random.choice(list(bigrams_list_dict.keys()))
#     while not start_word[0].isupper() or start_word[-1] in PUNCTUATION_MARKS:
#         start_word = random.choice(list(bigrams_list_dict.keys()))
#     output += start_word
#     for _j in range(4):
#         words = [x[0] for x in bigrams_list_dict[start_word].most_common()]
#         frequency = [x[1] for x in bigrams_list_dict[start_word].most_common()]
#         next_word = random.choices(words, frequency)[0]
#         if start_word[-1] in PUNCTUATION_MARKS:
#             while  not next_word[0].isupper():
#                 next_word = random.choices(words, frequency)[0]
#         output = output + " " + next_word
#         start_word = next_word
#     while start_word[-1] not in PUNCTUATION_MARKS:
#         words = [x[0] for x in bigrams_list_dict[start_word].most_common()]
#         frequency = [x[1] for x in bigrams_list_dict[start_word].most_common()]
#         next_word = random.choices(words, frequency)[0]
#         output = output + " " + next_word
#         start_word = next_word
#     print(output)

#------------------------------------STAGE 6------------------------------------
from nltk.tokenize import WhitespaceTokenizer
from nltk import trigrams
from collections import Counter
import random

PUNCTUATION_MARKS = ['.', '!', '?']

file_name = input()

tk = WhitespaceTokenizer()
with open(file_name, 'r', encoding='utf-8') as reader:
    tokens = tk.tokenize(reader.read())
trigrams_list = list(trigrams(tokens))
# print(trigrams_list[:10])

bigrams_list = [[x[0] + " " + x[1], x[2]] for x in trigrams_list]
# print(bigrams_list[:10])

bigrams_list_dict = {}
for bigram in bigrams_list:
    bigrams_list_dict.setdefault(bigram[0], []).append((bigram[1]))

for bigram_key in bigrams_list_dict.keys():
    bigrams_list_dict[bigram_key] = Counter(bigrams_list_dict[bigram_key])

for _i in range(10):
    output = ""
    start_word = random.choice(list(bigrams_list_dict.keys()))
    while not start_word[0].isupper() or start_word.split()[0][-1] in PUNCTUATION_MARKS:
        start_word = random.choice(list(bigrams_list_dict.keys()))
    output += start_word
    for _j in range(3):
        words = [x[0] for x in bigrams_list_dict[start_word].most_common()]
        frequency = [x[1] for x in bigrams_list_dict[start_word].most_common()]
        next_word = random.choices(words, frequency)[0]
        if start_word[-1] in PUNCTUATION_MARKS:
            while not next_word[0].isupper():
                next_word = random.choices(words, frequency)[0]
        output = output + " " + next_word
        start_word = start_word.split()[1] + " " + next_word
    while start_word[-1] not in PUNCTUATION_MARKS:
        words = [x[0] for x in bigrams_list_dict[start_word].most_common()]
        frequency = [x[1] for x in bigrams_list_dict[start_word].most_common()]
        next_word = random.choices(words, frequency)[0]
        output = output + " " + next_word
        start_word = start_word.split()[1] + " " + next_word
    print(output)