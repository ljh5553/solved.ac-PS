import sys

def dfs(r, c):
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    
    visited[r][c] = 1
    global compsize
    compsize += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if matrix[nr][nc] == "1" and visited[nr][nc] == 0:
                dfs(nr, nc)

N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(sys.stdin.readline().strip())

visited = [[0 for _ in range(N)] for _ in range(N)]
compsize = 0
rst = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == "1" and visited[i][j] == 0:
            compsize = 0
            dfs(i, j)
            rst.append(compsize)

rst.sort()
print(len(rst))
for item in rst:
    print(item)