'''
아이디어 : 11053 - 가장 긴 증가하는 부분 순열 문제와 매우 유사. DP문제

시간복잡도 : n^2

자료구조 : dp를 저장할 리스트
'''

import sys

N = int(sys.stdin.readline())
soldier = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(i):
        if soldier[j] > soldier[i]: dp[i] = max(dp[i], dp[j]+1)
print(N - max(dp))