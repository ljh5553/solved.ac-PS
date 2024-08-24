'''
https://www.acmicpc.net/problem/4179 - 불!

소요시간 29분, 풀이실패, 정답 아이디어를 유튜브 강의로 본 뒤 풀었음

아이디어 : DFS, 지훈이와 불에 대해 각각 DFS를 실행한 후 불이 퍼지는 시간을 먼저 파악한 후 지훈이를 움직임

시간복잡도 : O(V log E) V = 1000000 E = 4

자료구조 : DFS용 큐, 지도 2차원리스트, 불이 퍼질 2차원리스트

느낀점 : 현재 행과 열 다음 행과 열을 변수 헷갈리지 않게 조심해야함
         벽을 판정하는 조건을 꼼꼼히 봐야함
         불이 2개 이상 있을 수 있다는 경우를 캐치하지 못했으니 조건을 잘 봐야함
'''

import sys
from collections import deque

def bfs(q1, q2):
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    maxrow, maxcol = len(matrix), len(matrix[0])
    
    while q1:
        r, c = q1.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < maxrow and 0 <= nc < maxcol:
                if visited_f[nr][nc] == -1 and matrix[nr][nc] != "#":
                    visited_f[nr][nc] = visited_f[r][c] + 1
                    q1.append((nr, nc))

    while q2:
        r, c = q2.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 > nr or nr >= maxrow or 0 > nc or nc >= maxcol:
                print(visited_j[r][c] + 1)
                return

            if visited_j[nr][nc] == -1 and matrix[nr][nc] != "#":
                if visited_f[nr][nc] == -1 or visited_f[nr][nc] > visited_j[r][c] + 1:
                    visited_j[nr][nc] = visited_j[r][c] + 1
                    q2.append((nr, nc))
    
    print("IMPOSSIBLE")

R, C = map(int, sys.stdin.readline().split())
matrix = list()
for _ in range(R):
    matrix.append(sys.stdin.readline().strip())

visited_j = [[-1 for _ in range(C)] for _ in range(R)]
visited_f = [[-1 for _ in range(C)] for _ in range(R)]

q1 = deque()
q2 = deque()

for i in range(R):
    for j in range(C):
        if matrix[i][j] == "F":
            q1.append((i, j))
            visited_f[i][j] = 0
        if matrix[i][j] == "J":
            q2.append((i, j))
            visited_j[i][j] = 0

bfs(q1, q2)