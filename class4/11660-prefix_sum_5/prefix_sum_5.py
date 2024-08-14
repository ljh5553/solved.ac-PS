'''
아이디어 : DP. 2차원 배열의 부분합 (x1 x2 y1 y2) -> x2 y2의 부분합 - x2 y1-1의 부분합 - x1-1 y2의 부분합 + x1-1 y1-1의 부분합

시간복잡도 :

자료구조 : dp저장용 2차원리스트
'''

import sys

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + matrix[i-1][j-1]

for _ in range(M):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    print(dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1])