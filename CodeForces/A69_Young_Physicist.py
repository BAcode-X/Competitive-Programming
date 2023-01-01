x, y, z = 0, 0, 0
for i in range(int(input())):
    a, b, c = map(int, input().split())
    x += a
    y += b
    z += c
print("YES" if x == y == z == 0 else "NO")
