'''
https://www.acmicpc.net/problem/12865 - 평범한 배낭

소요시간 X분, 풀이X, 구글링 후 구현

아이디어 : DP행렬에서 행은 무게,가치(리스트로 구현), 열은 그 인덱스까지 담을 수 있는 무게(0이면 0kg까지, 4이면 4kg까지)
           값은 지금까지의 행(인덱스까지의 물건들)과 열에 따른 최대 가치를 나타냄

           현재 물건의 무게가 지금까지 담을 수 있는 무게(열)보다 크다면 지금 물건을 못 넣으므로
           바로 직전 물건으로 담을 수 있는 가치를 가져옴 (즉, dp[i][j] = dp[i-1][j])

           현재 물건의 무게가 지금까지 담을 수 있는 무게보다 크다면,
           바로 직전 물건으로 담을 수 있는 가치(dp[i-1][j])와
           현재 물건 무게를 뺀 최댓값(dp[i-1][j-bag[i-1][0]])과 현재 물건의 가치(bag[i-1][1])를
           더한 값을 비교해 더 큰 값으로 저장함 (즉, max(dp[i-1][j], dp[i-1][j-bag[i-1][0]]+bag[i-1][1]) )

시간복잡도 : 

자료구조 : dp 2차원리스트

느낀점 : DP문제라는 것과 대강의 풀이방법은 알고있었지만 잘 몰랐기에 처음부터 검색해서 공부한 뒤 구현함
'''

import sys

N, K = map(int, sys.stdin.readline().split())
bag = []
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    bag.append([W, V])

dp = [[0 for _ in range(K+1)] for _ in range(len(bag)+1)]
for i in range(len(bag)+1): dp[i][0] = 0
for i in range(K+1): dp[0][i] = 0

for i in range(1, len(bag)+1):
    for j in range(1, K+1):
        if j >= bag[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bag[i-1][0]]+bag[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])