'''
https://www.acmicpc.net/problem/1504 - 특정한 최단 경로

소요시간 18분, 풀이성공

아이디어 : 다익스트라. 시작 - v1 - v2 - 끝 과 시작 v2 - v1 - 끝 두 가지의 경로를 구한 뒤 최소거리를 선택

시간복잡도 : O(V log E)

자료구조 : 다익스트라용 우선순위큐

느낀점 : 다익스트라 알고리즘을 이용해서 각 지점까지 가는 거리를 쪼갠 뒤 합하면 된다

         풀이와는 별개로 문제를 잘 읽어봐야한다.
         가능한 경우가 없으면 -1 출력인데 이걸 못 봐서 한 번 틀렸습니다가 나옴
'''

import sys
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(s, e):
    dist = [sys.maxsize for _ in range(N+1)]
    pq = [(0, s)]
    dist[s] = 0

    while pq:
        w1, v = heappop(pq)

        if w1 > dist[v]: continue

        for w2, i in graph[v]:
            if w1+w2 < dist[i]:
                dist[i] = w1 + w2
                heappush(pq, (w1+w2, i))
    
    return dist[e]

N, E = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, sys.stdin.readline().split())

ans1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
ans2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if ans1 >= sys.maxsize and ans2 >= sys.maxsize: print(-1)
else: print(min(ans1, ans2))