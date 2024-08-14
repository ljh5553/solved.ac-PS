import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

c = list(set(X))
c.sort()
d = dict()

for i in range(len(c)):
    d[c[i]] = i

for item in X:
    print(d[item], end=" ")