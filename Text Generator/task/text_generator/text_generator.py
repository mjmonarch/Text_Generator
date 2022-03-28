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
from nltk.tokenize import WhitespaceTokenizer
from nltk import bigrams
from nltk import FreqDist

file_name = input()
tk = WhitespaceTokenizer()
with open(file_name, 'r', encoding='utf-8') as reader:
    tokens = tk.tokenize(reader.read())
    bigrams_list = list(bigrams(tokens))
    freq = FreqDist(bigrams_list)

print("Number of bigrams:", len(bigrams_list))

user_input = input()
while user_input != 'exit':
    try:
        num = int(user_input)
        if abs(num) >= len(bigrams_list):
            print("Index Error. Please input a value that is not greater than the number of all bigrams.")
        else:
            head = "{0:<18}".format("Head: " + bigrams_list[num][0])
            tail = "{0:<18}".format("Tail: " + bigrams_list[num][1])
            print(head, tail)
    except TypeError:
        print("Type Error: Please input an integer.")
    except ValueError:
        print("Value Error: Please input an integer.")
    user_input = input()
