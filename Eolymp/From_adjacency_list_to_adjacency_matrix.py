n = int(input())
grid = [[0 for _ in range(n)] for i in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(a[0]):
        grid[i][a[j+1]-1] = 1
for line in grid:
    print(*line)
