import sys

n = int(sys.stdin.readline())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = triangle[0][0]

cnt = 2
for i in range(1, n):
    for j in range(cnt):
        if j == 0: dp[i][j] = triangle[i][j] + dp[i-1][j]
        elif j == cnt-1: dp[i][j] = triangle[i][j] + dp[i-1][j-1]
        else: dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
        
    cnt += 1

print(max(dp[-1]))