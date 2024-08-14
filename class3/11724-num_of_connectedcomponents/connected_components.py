import sys
from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    if not graph.get(start): return

    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] != True:
                q.append(i)
                visited[i] = True

N, M = map(int, sys.stdin.readline().split())
graph = dict()
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    if not graph.get(a): graph[a] = [b]
    else: graph[a].append(b)

    if not graph.get(b): graph[b] = [a]
    else: graph[b].append(a)

rst = 0
visited = [False for _ in range(N+1)]
for i in range(1, N+1):
    if visited[i] != True:
        bfs(graph, i, visited)
        rst += 1

print(rst)