import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    dp = [0, 1, 2, 4]
    if n > 3:
        for i in range(4, n+1):
            dp.append(dp[i-3] + dp[i-2] + dp[i-1])
    print(dp[n])