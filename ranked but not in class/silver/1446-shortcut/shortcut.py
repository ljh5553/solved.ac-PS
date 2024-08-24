'''
https://www.acmicpc.net/problem/1446 - 지름길

소요시간 30분 초과, 풀이실패, 정답구글링 O

아이디어 : 0부터 D까지 지름길의 길이가 작은 것부터 최소힙에서 꺼내고 남은 거리를 더해주기

시간복잡도 : O(V + E log V) V=10000 E=9999+12

자료구조 : 우선순위큐를 구현할 최소힙, 그래프를 저장할 리스트, 거리정보를 저장할 리스트

느낀점 : 길이 하나하나마다를 노드로 봐야한다
         이 문제는 DP로도 풀이가 가능하다
'''

import sys
from heapq import heappop, heappush

def dijkstra(graph, start):
    pq = []
    heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        w1, v = heappop(pq)
        if w1 > dist[v]: continue

        for i, w2 in graph[v]:
            if w1 + w2 < dist[i]:
                dist[i] = w1 + w2
                heappush(pq, (w1+w2, i))
    
    print(dist[D])

N, D = map(int, sys.stdin.readline().split())
g = [[] for _ in range(D+1)]

for i in range(D):
    g[i].append((i+1, 1))

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    if b <= D: g[a].append((b, c))

dist = [sys.maxsize for _ in range(D+1)]
dijkstra(g, 0)