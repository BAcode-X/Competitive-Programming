for i in range(int(input())):
    n, c = input().split()
    s = input() * 2
    m = 0
    f = False
    cnt = 0
    for j in s:
        if j == c:
            f = True
        elif j == 'g' and f:
            m = max(cnt, m)
            cnt = 0
            f = False
        if f:
            cnt += 1
    print(m)
