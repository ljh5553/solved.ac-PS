import sys
from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = [start]

    while q:
        v = q.popleft()

        # bfs문제의 포인트 : 엣지가 없는 예외경우를 생각해줘야함
        if not graph.get(v): return 0
        
        for i in graph[v]:
            if i not in visited:
                q.append(i)
                visited.append(i)

    return(len(visited)-1)


graph = {}
N = int(sys.stdin.readline())
E = int(sys.stdin.readline())
for _ in range(E):
    a, b = map(int, sys.stdin.readline().split())
    if not graph.get(a): graph[a] = [b]
    else: graph[a].append(b)
    if not graph.get(b): graph[b] = [a]
    else: graph[b].append(a)

print(bfs(graph, 1))