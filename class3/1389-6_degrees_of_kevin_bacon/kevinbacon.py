'''
아이디어 : 2중 for를 통해 모든 사람과 모든 목적지에 대해 bfs

시간복잡도 : O(V+E), V = 100 E = 5000. 5100 < 2억

자료구조 : 그래프를 담는 딕셔너리, 방문경우를 담는 2차원리스트, 케빈베이컨수를 저장할 리스트

느낀점 : 탐색의 깊이를 저장해야 할 때는 큐에 튜플형태로 같이 넣은 뒤 다음 큐에 넣을 때 증가시킨다
'''

import sys
from collections import deque

def bfs(graph, start):
    q = deque([(start, 1)])
    visited[start][start] = 1

    while q:
        v, depth = q.popleft()

        for i in graph[v]:
            if visited[start][i] == 0:
                visited[start][i] = depth
                q.append((i, depth+1))
    
    visited[start][start] = 0
    kv.append(sum(visited[start]))

N, M = map(int, sys.stdin.readline().split())
graph = dict()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    if not graph.get(a): graph[a] = [b]
    else:
        if b not in graph[a]: graph[a].append(b)
    if not graph.get(b): graph[b] = [a]
    else:
        if a not in graph[b]: graph[b].append(a)
    
visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
kv = []

for i in range(1, N+1):
    bfs(graph, i)

print(kv.index(min(kv)) + 1)