import sys
    
N, M = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))

s, e = 1, max(h)

while s <= e:
    m = (s+e) // 2

    rst = 0

    for i in h:
        if i >= m:
            rst += i - m
    
    if rst >= M:
        s = m + 1
    else:
        e = m - 1

print(e)