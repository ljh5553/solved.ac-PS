'''
https://www.acmicpc.net/problem/11403 - 경로 찾기

아이디어 : DFS를 이용해 방문리스트에 방문을 저장하고 그 리스트를 출력, 결국 방문리스트가 갈 수 있는 경우의 수가 됨

시간복잡도 : O(V+E) V=100 E=V*(V-1)

자료구조 : 인접행렬저장용 2차원리스트, 결과저장용 2차원리스트, 방문확인용 리스트

느낀점 : 평소엔 자기 자신을 방문하지 않도록 초기값을 bfs의 큐에 넣은 뒤 방문체크했으나
         이번엔 자기 자신에게 돌아오는 경우를 생각해 방문체크를 하면 안 됐음
'''

import sys
from collections import deque

def bfs(start):
    q = deque([start])

    # 자기 자신에게 돌아오는 경우의 수도 체크해야하므로 방문처리 하면 안 됨
    #visited[start] = 1

    while q:
        v = q.popleft()

        for i in range(N):
            if adj_m[v][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)

N = int(sys.stdin.readline())
adj_m = list()
for _ in range(N):
    adj_m.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    visited = [0 for _ in range(N)]
    bfs(i)
    print(*visited)