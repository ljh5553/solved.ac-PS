import sys

coord = []
N = int(sys.stdin.readline())
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coord.append([x, y])

coord.sort(key=lambda x: (x[0], x[1]))
for i in coord:
    print(i[0], i[1])