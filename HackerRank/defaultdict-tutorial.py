from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())
for i in range(1, n+1):
    d[input()].append(i)
for i in range(m):
    a = input()
    if d[a]:
        print(*d[a])
    else:
        print(-1)
