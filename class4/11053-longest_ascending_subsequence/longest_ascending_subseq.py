'''
아이디어 : DP. 버블소트처럼 각각 현재 값과 이전 값들을 비교해본 뒤 현재dp위치값과 이전dp위치의 값 + 1 중 더 큰 것을 저장

시간복잡도 : n^2

자료구조 : DP 1차원리스트
'''

import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(i):
        if sequence[i] > sequence[j]: dp[i] = max(dp[i], dp[j]+1)

print(max(dp))