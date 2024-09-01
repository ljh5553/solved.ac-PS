'''
https://www.acmicpc.net/problem/1926 - 그림

소요시간 11분, 풀이성공

아이디어 : BFS, 주어진 2차원배열의 원소를 모두 탐색하며 방문하지 않은 1을 발견할 경우 시작점으로 BFS 후 개수 1 증가
           BFS을 하면서 방문하지 않은 1의 개수를 세어가면서 기존 크기값이랑 비교해 더 크면 갱신

시간복잡도 : O(V+E), V=250000 E=4

자료구조 : BFS용 큐

느낀점 : 기초적인 BFS문제여서 개수 카운터를 bfs실행시마다 1씩 올리고
         연결된 노드를 찾을 때마다 크기 카운터를 1씩 올려주면 되니 어려운 것은 없었음
'''

import sys
from collections import deque

def bfs(sr, sc):
    global ans
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    temp = 1

    q = deque([(sr, sc)])
    visited[sr][sc] = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 > nr or nr >= N or 0 > nc or nc >= M: continue
            if visited[nr][nc] == 1: continue

            if matrix[nr][nc] == 1:
                q.append((nr, nc))
                visited[nr][nc] = 1
                temp += 1
    
    ans = max(ans, temp)

N, M = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))


ans = cnt = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, ans)