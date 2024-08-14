import sys
from collections import deque

def bfs(graph, start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    row, col = len(graph), len(graph[0])

    q = deque([(start_x, start_y)])
    visited = [(start_x, start_y)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < row and 0 <= ny < col:
                if (nx, ny) not in visited:
                    if graph[nx][ny] == 1:
                        q.append((nx, ny))
                        visited.append((nx, ny))
                        graph[nx][ny] = graph[x][y] + 1

    return graph[row-1][col-1]

maze = []
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))

print(bfs(maze, 0, 0))