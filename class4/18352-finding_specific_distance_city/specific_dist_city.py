'''
https://www.acmicpc.net/problem/18352 - 특정 거리의 도시 찾기

소요시간 10분, 풀이성공, 정답구글링 X

아이디어 : 방향그래프에서 다른 노드까지의 최단거리를 찾은 뒤 조건에 맞는 최단거리만 출력

시간복잡도 : O(V + E log V)

자료구조 : 거리저장용 리스트, 그래프 인접리스트용 리스트, 우선순위 큐를 위한 최소힙

느낀점 : 가중치가 1로 고정이었는데 단순히 w2 부분을 1로 치환해서 풀이에 성공함
'''

import sys
from heapq import heappop, heappush

def dijkstra(graph, start):
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        w, v = heappop(pq)

        if w > dist[v]: continue

        for i in graph[v]:
            if w + 1 < dist[i]:
                heappush(pq, (w + 1, i))
                dist[i] = w + 1

V, E, K, X = map(int, sys.stdin.readline().split())
g = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)

dist = [sys.maxsize for _ in range(V+1)]
dijkstra(g, X)

flag = True
for i in range(1, V+1):
    if dist[i] == K:
        print(i)
        flag = False

if flag: print(-1)