import sys
from collections import deque

def bfs(graph, startr, startc, h):
    q = deque([(startr, startc)])
    visited[startr][startc] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    maxlen = len(graph)

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < maxlen and 0 <= nc < maxlen and visited[nr][nc] == 0:
                if graph[nr][nc] > h:
                    q.append((nr, nc))
                    visited[nr][nc] = 1

N = int(sys.stdin.readline())
matrix = []
min_h, max_h = 101, 0
for _ in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    for item in li:
        if min_h > min(li): min_h = min(li)
        if max_h < max(li): max_h = max(li)
    matrix.append(li)

rst = [1 for _ in range(max_h+1)]

for h in range(min_h, max_h):
    cnt = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and matrix[i][j] > h:
                bfs(matrix, i, j, h)
                cnt += 1
    rst[h] = cnt

print(max(rst))