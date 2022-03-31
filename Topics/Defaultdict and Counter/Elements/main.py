from collections import Counter

inp = input().lower().split()

counter_dict = Counter(inp)
print(sorted(counter_dict.elements()))
