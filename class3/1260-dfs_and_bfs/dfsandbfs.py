import sys
from collections import deque

def dfs(graph, start, visited=[]):
    visited.append(start)

    if not graph[start]: return visited

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

def bfs(graph, start):
    q = deque([start])
    visited = [start]

    if not graph[start]: return visited
    
    while q:
        node = q.popleft()
        for i in graph[node]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    return visited


N, M, V = map(int, sys.stdin.readline().split())

G = {}
for i in range(1, N+1):
    G[i] = []

for _ in range(M):
    e1, e2 = map(int, sys.stdin.readline().split())
    G[e1].append(e2)
    G[e2].append(e1)
    
for item in G: G[item].sort()

dfs_rst = dfs(G, V)
bfs_rst = bfs(G, V)

for i in dfs_rst: print(i, end=" ")
print()
for i in bfs_rst: print(i, end=" ")