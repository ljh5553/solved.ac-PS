'''
https://www.acmicpc.net/problem/9251 - LCS

소요시간 20분, 풀이실패, 이후 구글링으로 풀이 참조

아이디어 : DP. 같은 문자일 경우엔 대각선 왼쪽 위에서 1을 더한 값을 저장하고
           다른 문자일 경우엔 위와 왼쪽에서 가장 큰 값을 그대로 가져온다

           최장공통부분수열 자체를 찾고싶다면 DP테이블을 다 만든 뒤 가장 오른쪽 끝에서부터 시작해
           위와 왼쪽이 같은지 확인 후, 같다면 그 방향으로 움직이고 다르면 대각선 위로 움직이며
           대각선 위로 간 시점에서의 그 문자를 뒤에서부터 넣으면 된다

시간복잡도 : 

자료구조 : dp 테이블

느낀점 : LCS는 알고리즘 강의에서 다뤘던 내용이라 어렴풋이 기억하고 있었는데
         같은 문자를 찾았을 때 dp[i-1][j-1]+1 를 해야하는걸 max(dp[i-1][j], dp[i][j-1])+1 을 해서 틀렸다
         오랜만에 봐도 어느정도 기억이 났다는 점에서 위안삼아야겠다
'''

import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
for i in range(len(str1)+1):
    dp[0][i] = 0
for i in range(len(str2)+1):
    dp[i][0] = 0

for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):
        if str2[i-1] == str1[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])