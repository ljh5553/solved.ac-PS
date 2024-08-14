import sys, heapq

h = []
N = int(sys.stdin.readline())
for _ in range(N):
    c = int(sys.stdin.readline())

    if c == 0:
        if len(h) == 0: print("0")
        else: print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (-c, c))