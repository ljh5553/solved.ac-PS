import sys
from collections import deque

def bfs(g, start_x, start_y):
    row, col = len(g), len(g[0])
    sol = [[-1 for _ in range(col)] for _ in range(row)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque([(start_x, start_y)])
    sol[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col:
                if sol[nx][ny] == -1:
                    if g[nx][ny] == 0:
                        sol[nx][ny] = 0
                    elif g[nx][ny] == 1:
                        q.append((nx, ny))
                        sol[nx][ny] = sol[x][y] + 1
    
    for i in range(row):
        for j in range(col):
            if g[i][j] == 0: print("0", end=" ")
            else: print(sol[i][j], end=" ")
        print()

r, c = map(int, sys.stdin.readline().split())
m = []

for i in range(r):
    l = list(map(int, sys.stdin.readline().split()))
    m.append(l)

    if 2 in l: x, y = i, l.index(2)

bfs(m, x, y)