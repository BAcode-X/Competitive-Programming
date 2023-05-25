cnt = 0
for i in range(int(input())):
    a = list(map(int, input().split()))
    cnt += a.count(1)
print(cnt//2)
