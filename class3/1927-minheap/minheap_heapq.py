import sys, heapq

N = int(sys.stdin.readline())
h = []
for _ in range(N):
    x = int(sys.stdin.readline())
    
    if x != 0: heapq.heappush(h, x)
    else:
        if len(h) == 0: print("0")
        else: print(heapq.heappop(h))