from collections import Counter

all_w = []

for i in range(int(input())):
    all_w.append(input())

occurance = Counter(all_w)

n = len(occurance)
print(n)

for word in set(all_w):
    print(occurance[word], end=' ')
