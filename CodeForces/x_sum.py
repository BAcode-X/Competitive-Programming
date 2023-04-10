def diag_sum(arr, n, m, x, y):
    s = 0
    i, j = x, y
    # up  right
    while i > -1 and j < m:
        s += arr[i][j]
        i -= 1
        j += 1
    # up left
    i, j = x, y
    while i > -1 and j > -1:
        s += arr[i][j]
        i -= 1
        j -= 1
    # down right
    i, j = x, y
    while i < n and j < m:
        s += arr[i][j]
        i += 1
        j += 1
    # down left
    i, j = x, y
    while i < n and j > -1:
        s += arr[i][j]
        i += 1
        j -= 1
    return s - (arr[x][y]*3)

for _ in range(int(input())):
    n, m = map(int, input().split())
    board = []
    for k in range(n):
        board.append(list(map(int, input().split())))
    mx = 0   
    for i in range(n):
        for j in range(m):
            v = diag_sum(board, n, m, i, j)
            mx = max(mx, v)
    print(mx)
