'''
아이디어 : 좌표 내에서 본인위치를 찾고 BFS를 통해 찾을 수 있는 모든 P의 개수 구하기

시간복잡도 : O(V+E), V = NM, E = 4NM. 360000*4 < 2억

자료구조 : 캠퍼스지도 2차원배열, 방문기록 2차원배열, 사람만난 카운터
'''

import sys
from collections import deque

def bfs(startr, startc):
    q = deque([(startr, startc)])
    visited[startr][startc] = 1

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    cnt = 0

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] in ("O", "P") and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    if matrix[nr][nc] == "P": cnt += 1
    
    return cnt

N, M = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(sys.stdin.readline().strip())

visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == "I":
            rst = bfs(i, j)

if rst == 0: print("TT")
else: print(rst)