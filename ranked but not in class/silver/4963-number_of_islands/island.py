'''
아이디어 : 지도의 각 좌표에 대해 DFS, 연결부분들을 카운팅

시간복잡도 : O(V+E). V = w*h, E = 8*w*h. 22500 < 2억

자료구조 : 지도저장 2차원배열, 방문저장 2차원배열, 섬 개수 카운터

주의사항 : 대각선으로도 이동가능
'''


import sys
sys.setrecursionlimit(10**6)

def dfs(r, c):
    dr = [0, 0, -1, 1, -1, -1, 1, 1]
    dc = [-1, 1, 0, 0, -1, 1, -1, 1]

    visited[r][c] = 1

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < h and 0 <= nc < w:
            if matrix[nr][nc] == 1 and visited[nr][nc] == 0:
                dfs(nr, nc)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0 : break

    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

    visited = [[0 for _ in range(w)] for _ in range(h)]
    num_islands = 0

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                num_islands += 1
                dfs(i, j)

    print(num_islands)