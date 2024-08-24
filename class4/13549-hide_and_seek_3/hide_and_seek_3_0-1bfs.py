'''
https://www.acmicpc.net/problem/13549 - 숨바꼭질 3

소요시간 X분, 풀이X, 정답구글링으로 처음 구현해봄

아이디어 : 가중치가 0과 1로만 이루어진 그래프에서 최단 경로를 찾는 0-1 BFS 알고리즘
           우선순위가 높은 (가중치가 0인) 경로에 대해서는 덱을 사용해 앞 부분에 데이터를 넣고
           우선순위가 낮은 (가중치가 1인) 경로에 대해서는 일반 큐를 사용하듯이 뒷 부분에 데이터를 넣는다
           그러면 우선순위가 높은 경로를 최우선으로 탐색하게 되니 가장 낮은 비용의 경로를 찾을 수 있음

시간복잡도 : O(V + E) V = 100000 E = 2

자료구조 : 우선순위큐 구현용 최소힙, 거리저장용 리스트

느낀점 : *2는 가중치가 0이니 명확하게 우선순위를 알 수 있지만, -1이 +1보다 우선한다는 것은 알기 어렵다
         즉, 케이스를 잘 따져봐서 +1 한 뒤 *2를 하는 것보다 -1을 하고 *2를 하는 것이 더 효율적이라는 것을 캐치해야함
         예시로 3->10이 있다. +1 먼저 할 경우 3-6-7-8-9-10, -1 먼저 할 경우 3-6-5-10
'''

import sys
from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = 0

    while q:
        v = q.popleft()

        if v == K:
            print(visited[v])
            return

        for i in (v-1, v+1, v*2):
            if 0 <= i < 100001 and visited[i] == -1:
                if i == v*2:
                    q.appendleft(i)
                    visited[i] = visited[v]
                else:
                    q.append(i)
                    visited[i] = visited[v] + 1

N, K = map(int, sys.stdin.readline().split())
visited = [-1 for _ in range(100001)]
bfs(N)