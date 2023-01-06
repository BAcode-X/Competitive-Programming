from collections import Counter
n = int(input())
rooms = list(map(int, input().split()))
rep = list(Counter(rooms).items())
for i in rep:
    if i[1] == 1:
        print(i[0])
        break
