'''
https://www.acmicpc.net/problem/17070 - 파이프 옮기기 1

소요시간 X분, 풀이X, 구글링 후 구현

아이디어 : 

시간복잡도 : 

자료구조 : 

느낀점 : 처음 목표로 했던 풀이법이었다. bfs를 이용한 길 찾기로, 나는 이전 파이프의 점을 모두 파라미터로 넘겨서
         x와 y의 차이로 상태를 판단했고 그것을 기반으로 또 각각 가로 세로 대각선의 경우의 수를 찾으려고 했다

         이 코드는 큐에 현재 상태를 미리 정한 상태로 넣고, 그 상태에 따라 다시 경우의 수를 저장하며 큐에 넣는다
         큰 틀에서는 같지만 형태를 미리 정의해서 넣으니 코드가 훨씬 간결해짐
'''

import sys
from collections import deque

def bfs(sr, sc, state): # state : 0이면 가로, 1이면 세로, 2이면 대각
    global ans
    q = deque([(sr, sc, state)])

    while q:
        r, c, s = q.popleft()

        if r == N-1 and c == N-1:
            ans += 1
            continue

        if s == 0:
            if c == N-1: continue

            if 0 <= r < N and 0 <= c+1 < N and matrix[r][c+1] == 0:
                q.append((r, c+1, 0))
            
            if 0 <= r+1 < N and 0 <= c+1 < N and matrix[r][c+1] == 0 and matrix[r+1][c] == 0 and matrix[r+1][c+1] == 0:
                q.append((r+1, c+1, 2))

        if s == 1:
            if r == N-1: continue

            if 0 <= r+1 < N and 0 <= c < N and matrix[r+1][c] == 0:
                q.append((r+1, c, 1))
            
            if 0 <= r+1 < N and 0 <= c+1 < N and matrix[r][c+1] == 0 and matrix[r+1][c] == 0 and matrix[r+1][c+1] == 0:
                q.append((r+1, c+1, 2))

        if s == 2:
            if 0 <= r < N and 0 <= c+1 < N and matrix[r][c+1] == 0:
                q.append((r, c+1, 0))

            if 0 <= r+1 < N and 0 <= c < N and matrix[r+1][c] == 0:
                q.append((r+1, c, 1))

            if 0 <= r+1 < N and 0 <= c+1 < N and matrix[r][c+1] == 0 and matrix[r+1][c] == 0 and matrix[r+1][c+1] == 0:
                q.append((r+1, c+1, 2))
    
N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

ans = 0
bfs(0, 1, 0)
print(ans)