import sys
from collections import deque

def bfs(matrix, startr, startc, v, flag):
    q = deque([(startr, startc)])
    v[startr][startc] = 1

    maxlen = len(matrix)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < maxlen and 0 <= nc < maxlen:
                if flag == 0:
                    if v[nr][nc] == 0 and matrix[nr][nc] == matrix[r][c]:
                        v[nr][nc] = 1
                        q.append((nr, nc))
                else:
                    blind = ["R", "G"]
                    if v[nr][nc] == 0:
                        if matrix[nr][nc] == matrix[r][c]:
                            v[nr][nc] = 1
                            q.append((nr, nc))
                        elif matrix[nr][nc] in blind and matrix[r][c] in blind:
                            v[nr][nc] = 1
                            q.append((nr, nc))


N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(sys.stdin.readline().strip())

cnt_normal, cnt_blind = 0, 0

visited_normal = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited_normal[i][j] == 0:
            bfs(matrix, i, j, visited_normal, 0)
            cnt_normal += 1

visited_blind = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited_blind[i][j] == 0:
            bfs(matrix, i, j, visited_blind, 1)
            cnt_blind += 1

print(cnt_normal, cnt_blind)