import sys

N = int(sys.stdin.readline())

dp = [-1, 0]

if N > 1:
    for i in range(2, N+1):
        m1, d2, d3 = 100, 100, 100

        m1 = 1 + dp[i-1]
        if i%2 == 0:
            d2 = 1 + dp[i//2]
        if i%3 == 0:
            d3 = 1 + dp[i//3]
        dp.append(min(m1, d2, d3))

print(dp[N])