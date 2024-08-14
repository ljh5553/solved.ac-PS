'''
아이디어 : 좌표 내에서 본인위치를 찾고 DFS를 통해 찾을 수 있는 모든 P의 개수 구하기

시간복잡도 : O(V+E), V = NM, E = 4NM. 360000*4 < 2억

자료구조 : 캠퍼스지도 2차원배열, 방문기록 2차원배열, 사람만난 카운터
'''

import sys
sys.setrecursionlimit(10**6)

def dfs(startr, startc):
    visited[startr][startc] = 1

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    global cnt

    for i in range(4):
        nr = startr + dr[i]
        nc = startc + dc[i]

        if 0 <= nr < N and 0 <= nc < M:
            if matrix[nr][nc] in ("O", "P") and visited[nr][nc] == 0:
                if matrix[nr][nc] == "P": cnt += 1
                dfs(nr, nc)

N, M = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(sys.stdin.readline().strip())

visited = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] == "I":
            dfs(i, j)

if cnt == 0: print("TT")
else: print(cnt)