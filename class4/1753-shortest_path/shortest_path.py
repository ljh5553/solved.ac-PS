'''
https://www.acmicpc.net/problem/1753 - 최단경로

소요시간 x분, 풀이실패, 정답구글링 O, 다익스트라로 처음 풀어보는 문제라 다른 자료 참고해서 품

아이디어 : 한 정점에서 다른 경로로 가는 최단거리이므로 다익스트라 알고리즘

시간복잡도 : O(V + E log V)

자료구조 : 다익스트라를 위한 우선순위큐, 인접리스트용 리스트, 거리저장용 리스트

느낀점 : 처음에 계속 시간초과가 나서 뭔가했더니 우선순위큐인 pq에 넣을 때 첫 번째 값으로 비용을 넣어줘야한다
         코드의 일관성을 위해 첫 번째 값으로 start를 넣었더니 답은 잘 나와도 거리가 짧은 순서대로 나오지 않아 시간초과가 발생함
'''

import sys
from heapq import heappush, heappop

def dijkstra(graph, start):
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        w1, v = heappop(pq)

        # 지금 꺼낸 거리 코스트가 지금까지 찾은 최단거리보다 크면 탐색이 의미가 없음
        if dist[v] < w1: continue

        for i, w2 in graph[v]:
            if w1 + w2 < dist[i]:
                heappush(pq, (w1 + w2, i))
                dist[i] = w1 + w2

V, E = map(int, sys.stdin.readline().split())
s = int(sys.stdin.readline())
g = [[] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append((b, c))

dist = [sys.maxsize for _ in range(V+1)]
dijkstra(g, s)

for i in range(1, V+1):
    if dist[i] == sys.maxsize: print("INF")
    else: print(dist[i])