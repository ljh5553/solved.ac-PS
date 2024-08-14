import sys
from collections import deque

def bfs(graph, coord):
    q = deque(coord)
    visited = [[0 for _ in range(C)] for _ in range(R)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    row = len(graph)
    col = len(graph[0])
    n_max = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col:
                if graph[nx][ny] == 0:
                    if visited[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                        if visited[nx][ny] > n_max: n_max = visited[nx][ny]

    for i in range(row):
        for j in range(col):
            if visited[i][j] == 0 and graph[i][j] == 0:
                return -1
    return n_max

C, R = map(int, sys.stdin.readline().split())
m = []
coord = []
for i in range(R):
    m.append(list(map(int, sys.stdin.readline().split())))

for i in range(R):
    for j in range(C):
        if m[i][j] == 1: coord.append((i, j))

print(bfs(m, coord))