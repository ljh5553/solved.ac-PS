'''
https://www.acmicpc.net/problem/14500 - 테트로미노

소요시간 35분초과, 풀이실패, 풀이 방향을 구글링으로 알고있는 상태로 풀이했지만 다시찾아봄

아이디어 : DFS, ㅗ 모양 테트로미노 빼고는 모두 4번까지 탐색한 BFS로 만들어낼 수 있는 모양이다
           ㅗ 모양은 2번째 반복일 경우에 시작한 방향 빼고 나머지 방향 3개 중 2가지를 선택해 만들 수 있다

시간복잡도 : O(V log E) V = 500*500 E = 4

자료구조 : 

느낀점 : 처음에 BFS로 풀다가 DFS로 방향을 바꿔서 푸려고했는데 구현에 실패했다

         단순 DFS라기보다는 백트래킹 문제이다
         테트로미노를 만드는게 깊이우선탐색으로 4개를 채운 뒤 지금까지의 합을 최대값과 갱신하고
         마지막 블록을 빠져나와서 다시 다른 모양을 만들어보는 방법을 반복해야 하기 때문에
         백트래킹 형태로 풀이를 해야했다.

         ㅗ모양을 만드는건 일단 현재 위치를 중심으로 잡은 뒤 상우하 우하좌 하좌상 좌상우
         이렇게 4가지 경우의 수를 직접 더하면 알 수 있다

         풀면서 백트래킹이 아닌가 잠깐 생각하긴 했는데 무지성으로 단순히 만들었다가 놓쳤다
'''

import sys

def dfs(sr, sc, sd, ssum):
    global ans
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    if sd == 3:
        ans = max(ans, ssum)
        return

    for i in range(4):
        nr, nc = sr + dr[i], sc + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                dfs(nr, nc, sd+1, ssum+matrix[nr][nc])
                visited[nr][nc] = 0

def Tshape(sr, sc):
    global ans
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        tsum = matrix[sr][sc]
        for j in range(3):
            nr, nc = sr + dr[(i+j)%4], sc + dc[(i+j)%4]
            if 0 <= nr < N and 0 <= nc < M:
                tsum += matrix[nr][nc]
            else:
                tsum = -1
                break
        ans = max(ans, tsum)


N, M = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

visited = [[0 for _ in range(M)] for _ in range(N)]
ans = -1
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, matrix[i][j])
        visited[i][j] = 0
        Tshape(i, j)

print(ans)