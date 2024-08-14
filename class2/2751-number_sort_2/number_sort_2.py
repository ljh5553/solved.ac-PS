import sys

li = []
N = int(sys.stdin.readline())
for _ in range(N):
    li.append(int(sys.stdin.readline()))

li.sort()
for l in li:
    print(l)