'''
https://www.acmicpc.net/problem/13549 - 숨바꼭질 3

소요시간 12분, 풀이성공, 정답구글링 X

아이디어 : 다익스트라를 이용해 각 지점을 노드로 보고 최단거리 탐색, 가중치는 +1 -1 일 때 1이고 *2 일때는 0

시간복잡도 : O(E log V) V = 100000 E = 2

자료구조 : 우선순위큐 구현용 최소힙, 거리저장용 리스트

느낀점 : 각 지점이 노드라고 생각하는 두 번째 문제 (첫 번째는 1446-지름길)
         이 문제는 0-1 BFS 해결법으로도 풀 수 있다 (동일 폴더 내 hide_and_seek_3_0-1bfs.py 참조)
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
    
    print(dist[K])

N, K = map(int, sys.stdin.readline().split())
dist = [sys.maxsize for _ in range(100001)]
g = [[] for _ in range(100001)]

for i in range(100001):
    if i != 100000: g[i].append((i+1, 1))
    if i != 0: g[i].append((i-1, 1))

for i in range((100000//2)+1):
    g[i].append((i*2, 0))

dijkstra(g, N)