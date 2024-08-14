import sys

K, N = map(int, sys.stdin.readline().split())
lans = []
for _ in range(K):
    lans.append(int(sys.stdin.readline()))

s, e = 1, max(lans)

while s <= e:
    m = (s+e)//2
    rst = 0

    for lan in lans:
        rst += lan // m
    
    if rst >= N:
        s = m + 1
    elif rst < N:
        e = m - 1

print(e)