n, m = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
i, j = 0, 0
ans = []
while i < n and j < m:
    if a[i] < b[j]:
        ans.append(a[i])
        i += 1
    else:
        ans.append(b[j])
        j += 1
ans += a[i:]
ans += b[j:]
print(*ans)
