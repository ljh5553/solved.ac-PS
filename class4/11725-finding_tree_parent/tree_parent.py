import sys
from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited[start] = 1

    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = v

N = int(sys.stdin.readline())
graph = dict()
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())

    if not graph.get(a): graph[a] = [b]
    else: graph[a].append(b)
    if not graph.get(b): graph[b] = [a]
    else: graph[b].append(a)

visited = [0 for _ in range(N+1)]
bfs(graph, 1)
for i in range(2, N+1):
    print(visited[i])