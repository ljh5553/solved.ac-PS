'''
https://www.acmicpc.net/problem/1916 - 최소비용 구하기

소요시간 11분, 풀이성공, 정답구글링 x

아이디어 : 방향그래프에서 최소비용을 찾는 문제이므로 다익스트라

시간복잡도 : O(V + E log V)

자료구조 : 거리저장용 리스트, 그래프 인접리스트용 리스트, 우선순위 큐를 위한 최소힙

느낀점 : 변수를 헷갈려서 인덱스 자리에 이상한 변수를 안 넣게 주의
'''

import sys
from heapq import heappop, heappush

def dijkstra(graph, start):
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        w1, v = heappop(pq)

        if w1 > dist[v]: continue

        for i, w2 in graph[v]:
            if w1 + w2 < dist[i]:
                dist[i] = w1 + w2
                heappush(pq, (w1+w2, i))

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
g = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append((b, c))
s, d = map(int, sys.stdin.readline().split())

dist = [sys.maxsize for _ in range(N+1)]
dijkstra(g, s)

print(dist[d])