import sys
from collections import deque

def bfs(start):
    q = deque([start])
    visited = [0 for _ in range(MAX+1)]

    while q:
        v = q.popleft()

        if v == K: return visited[K]

        for i in (v+1, v-1, v*2):
            if 0 <= i <= MAX and not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1

N, K = map(int, sys.stdin.readline().split())

MAX = 10 ** 5
print(bfs(N))