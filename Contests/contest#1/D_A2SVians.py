from collections import Counter

_ = input()

all_m = input().split()
bad = Counter(input().split())
ex = 0
for j in all_m:
    if bad.get(j, None):
        continue
    k = Counter(list(j))
    d = list(k.values())
    n = d[0]
    flag = True
    for k in d:
        if k != n:
            flag = False
    if flag:
        ex += 1
print(ex)
