from collections import Counter

text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

freq_counter = Counter(text.split())

try:
    num = int(input())
    for tup in freq_counter.most_common(num):
        print(*tup)
except ValueError:
    print("You should enter numbers!")
