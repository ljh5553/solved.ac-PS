import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())

    zero_dp = [1, 0, 1]
    one_dp = [0, 1, 1]

    if N > 2:
        for i in range(3, N+1):
            zero_dp.append(zero_dp[i-2] + zero_dp[i-1])
            one_dp.append(one_dp[i-2] + one_dp[i-1])
    
    print(zero_dp[N], one_dp[N])