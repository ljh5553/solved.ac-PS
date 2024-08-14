import sys
from collections import deque

def bfs(graph, start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    row, col = len(graph), len(graph[0])

    graph[start_x][start_y] = 0
    q = deque([(start_x, start_y)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0


T = int(sys.stdin.readline())

for _ in range(T):
    col, row, K = map(int, sys.stdin.readline().split())
    rst = 0

    m = [[0 for _ in range(col)] for _ in range(row)]
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        m[x][y] = 1
    
    for i in range(row):
        for j in range(col):
            if m[i][j] == 1:
                bfs(m, i, j)
                rst += 1

    print(rst)