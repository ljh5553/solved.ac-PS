'''
아이디어 : dp, 6번째부터 1번째와 5번째 값의 합으로 새 값이 결정됨
           i > 5 일 때, dp[i] = dp[i-1] + dp[i-5]

시간복잡도 : ?

자료구조 : dp를 저장할 1차원리스트
'''

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    dp = [0, 1, 1, 1, 2, 2]
    N = int(sys.stdin.readline())
    if N <= 5: print(dp[N])
    else:
        for i in range(6, N+1):
            dp.append(dp[i-1] + dp[i-5])
        print(dp[N])