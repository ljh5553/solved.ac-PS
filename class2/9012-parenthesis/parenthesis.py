import sys

N = int(input())
for _ in range(N):
    p = sys.stdin.readline().strip()
    s = []
    top = -1
    for i in range(len(p)):
        top += 1
        s.append(p[i])
        if s[top] == ")" and s[top-1] == "(":
            s.pop()
            s.pop()
            top -= 2

    if s: print("NO")
    else: print("YES")