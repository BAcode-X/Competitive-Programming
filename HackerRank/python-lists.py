if __name__ == '__main__':
    N = int(input())
    a = []
    for i in range(N):
        cmd = input().strip().split()
        if cmd[0].strip() == 'print':
            print(a)
        elif cmd[0] == 'pop':
            a.pop()
        elif cmd[0] == 'sort':
            a.sort()
        elif cmd[0] == 'reverse':
            a.reverse()
        elif cmd[0] == 'append':
            a.append(int(cmd[1]))
        elif cmd[0] == 'remove':
            a.remove(int(cmd[1]))
        elif cmd[0] == 'insert':
            a.insert(int(cmd[1]), int(cmd[2]))
