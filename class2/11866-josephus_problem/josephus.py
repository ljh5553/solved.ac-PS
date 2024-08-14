import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, N+1)])
ans = []
for _ in range(N-1):
    for _ in range(K-1):
        q.append(q.popleft())
    ans.append(q.popleft())
ans.extend(q)

print("<", end='')
for i, a in enumerate(ans):
    if i == N-1: print(a, end=">")
    else: print(a, end=', ')