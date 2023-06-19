n = int(input())
grid = []
for i in range(n):
    line = list(map(int, input().split()))
    v = sum(line)
    pos = [v]
    if v:
        kk = [j+1 for j in range(n) if line[j]]
        pos.extend(kk)
    grid.append(pos)
    
for line in grid:
    print(*line)
