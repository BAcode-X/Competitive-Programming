from collections import defaultdict

graph = defaultdict(list)

n = int(input())
k = int(input())

for i in range(k):
    cmd, *val = list(map(int, input().split()))
    if cmd == 1:
        graph[val[0]].append(str(val[1]))
        graph[val[1]].append(str(val[0]))
    else:
        if graph[val[0]]:
            print(' '.join(graph[val[0]]))
