'''
아이디어 : DP. 첫 번째 열부터 최대가치를 메모이제이션하면서 나아감. 최댓값의 경우의 수는 2가지로, 다른 행의 바로 전 열이거나 두번째 전 열

시간복잡도 : ?

자료구조 : 메모이제이션용 2차원리스트
'''

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    stickers = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    dp = [[0 for _ in range(N+1)] for _ in range(2)]
    dp[0][1], dp[1][1] = stickers[0][0], stickers[1][0]

    for i in range(2, N+1):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + stickers[0][i-1]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + stickers[1][i-1]
    
    print(max(dp[0][-1], dp[1][-1]))