import sys
from collections import deque

def bfs(matrix, startr, startc):
    q = deque([(startr, startc)])
    visited[startr][startc] = 1
    cnt = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    rowmax = len(matrix)
    colmax = len(matrix[0])

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < rowmax and 0 <= nc < colmax:
                if visited[nr][nc] == 0 and matrix[nr][nc] == "1":
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    cnt += 1

    return cnt

N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(sys.stdin.readline().strip())

visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
rst = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "1" and visited[i][j] == 0:
            rst.append(bfs(matrix, i, j))

rst.sort()
print(len(rst))
for item in rst:
    print(item)