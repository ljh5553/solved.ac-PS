'''
https://www.acmicpc.net/problem/17626 - Four Squares

아이디어 : dp문제. 이전에 사용했던 제곱들을 반복해서 사용한다는 점에서 DP라는 점을 알아야함
           즉, 26의 해답을 구하려면, [26-1], [26-4], [26-9] [26-16] 을 비교한 뒤에 최소값을 취해서 가져옴
           이후 가져온 최소값에 1을 더해줌. 그 이유는 항상 제곱수가 더해지기때문
           (1, 4, 9, 16 같이 뺀 숫자들이 모두 제곱수이므로 증가할 때는 항상 1이 증가함)

           dp[i] = min(4, dp[i-각 제곱수]) + 1

시간복잡도 :

자료구조 : dp저장 리스트
'''

import sys

n = int(sys.stdin.readline())
dp = [0, 1]

for i in range(2, n+1):
    min_s = 4
    for j in range(1, int(i**0.5)+1):
        min_s = min(min_s, dp[i-j**2])
    dp.append(min_s + 1)

print(dp[n])