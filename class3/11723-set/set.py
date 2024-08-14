import sys

s = {}
N = int(sys.stdin.readline())
for _ in range(N):
    cmd = list(map(str, sys.stdin.readline().split()))
    if len(cmd) > 1: cmd[1] = int(cmd[1])

    if cmd[0] == "add":
        if not s.get(cmd[1]): s[cmd[1]] = True
    elif cmd[0] == "remove":
        if s.get(cmd[1]): del s[cmd[1]]
    elif cmd[0] == "check":
        if s.get(cmd[1]): print("1")
        else: print("0")
    elif cmd[0] == "toggle":
        if s.get(cmd[1]): del s[cmd[1]]
        else: s[cmd[1]] = True
    elif cmd[0] == "all":
        for i in range(1, 21):
            s[i] = True
    elif cmd[0] == "empty":
        s.clear()