'''
https://www.acmicpc.net/problem/2775 - 부녀회장이 될테야

소요시간 17분, 풀이성공

아이디어 : 브루트포스. 3중 반복문을 통해 각 행렬에 대해 이전 행의 현재 열까지 더해서 입력된 곳까지 구함

시간복잡도 : O(N^3) 14*14*14

자료구조 : 

느낀점 : k와 n의 최대치가 14로 작았기 때문에 3중 for문으로 구현해도
         충분히 시간복잡도 내에 들어갈 것이라고 생각했고 실제로도 정답이었다
'''

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    apt = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(1, n+1):
        apt[0][i] = i

    for i in range(1, k+1):
        for j in range(1, n+1):
            for l in range(1, j+1):
                apt[i][j] += apt[i-1][l]
    
    print(apt[k][n])