'''
아이디어 : dp문제. 마지막 계단에서 봤을 때 바로 전 계단에서왔는지 두번째 전 계단에서 왔는지 체크 후 최댓값 취해서 더하기
           즉, dp[i-3]+stairs[i-1]+stairs[i] 와 dp[i-2]+stairs[i] 중 최댓값을 취하면 됨
           첫 번째는 3번째 전까지 올라오는 최댓값+2칸연속밟기, 두 번째는 2번째 전까지 올라오는 최댓값+이번칸밟기
           첫 번째와 두 번째 계단의 DP는 직접 최댓값을 계산해줘야함

시간복잡도 : ?

자료구조 : 계단저장 리스트, DP값저장 리스트

느낀점 : dp를 할 때 초깃값에 대한 예외처리를 해줘야함
'''

import sys

N = int(sys.stdin.readline())
stairs = [0]
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

dp = [0 for _ in range(N+1)]

if N == 1: print(stairs[1])
elif N == 2: print(stairs[1] + stairs[2])
else:
    dp[1], dp[2] = stairs[1], stairs[1] + stairs[2]
    for i in range(3, N+1):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

    print(dp[N])