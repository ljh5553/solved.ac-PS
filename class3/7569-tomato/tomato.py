'''
https://www.acmicpc.net/problem/7569 - 토마토

소요시간 52분, 풀이성공

아이디어 : 기존 토마토문제에서 이동방향을 추가해주면 됨

시간복잡도 : O(V log E)

자료구조 : DFS를 위한 큐

느낀점 : 로직 자체는 진작에 맞혔는데 3차원리스트로 토마토를 저장하는 부분에서 문제가 생김
         처음엔 temp 리스트를 초기화시켜주지 않아 값이 중복되어 저장됐는데,
         clear() 메소드를 사용하니 tomatos까지 날아가는 현상이 발생함

         또한 출력 부분에서 for-else 문을 사용했는데
         break 체크를 잘못해 출력이 여러 번 되는 경우가 있었음
'''

import sys
from collections import deque

def bfs():
    global q, visited, ans

    dr = [-1, 0, 1, 0, 0, 0]
    dc = [0, 1, 0, -1, 0, 0]
    dh = [0, 0, 0, 0, -1, 1]
    maxr, maxc, maxh = len(tomatos[0]), len(tomatos[0][0]), len(tomatos)

    while q:
        h, r, c, day = q.popleft()
        ans = max(day, ans)

        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nh = h + dh[i]

            if 0 > nr or nr >= maxr or 0 > nc or nc >= maxc or 0 > nh or nh >= maxh: continue

            if visited[nh][nr][nc] != 1 and tomatos[nh][nr][nc] == 0:
                tomatos[nh][nr][nc] = 1
                q.append((nh, nr, nc, day + 1))

M, N, H = map(int, sys.stdin.readline().split())
temp = []
tomatos = []
for _ in range(H):
    for _ in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))
    tomatos.append(temp)
    temp = []

q = deque()
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
ans = 0

for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomatos[k][i][j] == 1:
                visited[k][i][j] = 1
                q.append((k, i, j, ans))

bfs()

isnotdone = False
for k in range(H):
    if isnotdone: break
    for i in range(N):
        if isnotdone: break
        for j in range(M):
            if tomatos[k][i][j] == 0:
                print(-1)
                isnotdone = True
                break
    
if not isnotdone: print(ans)