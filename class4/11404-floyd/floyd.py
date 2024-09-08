'''
https://www.acmicpc.net/problem/11404 - 플로이드

소요시간 X분, 풀이X, 구글링으로 플로이드-워셜 알고리즘을 처음 구현해봄

아이디어 : 플로이드-워셜 알고리즘. 모든 점에 대해 최소 경로를 구하는 알고리즘
           인접행렬을 무한값으로 초기화한 뒤 자기 자신은 0, 직접 연결된 각 경로는 그 값으로 초기화한 뒤
           k, i, j 순서대로 3중 반복문을 실행해 i-j와 i-k-j 중 작은 경로를 택해 나가는 DP적인 방식으로 최소경로를 구함

시간복잡도 : O(N^3)

자료구조 : 인접 행렬을 구현할 2차원리스트

느낀점 : 플로이드-워셜도 알고리즘 강의에서 들어서 어떤 것인지 대강은 알고있었지만
         자세히 기억이 안 나 구글링을 통해 다시 보고 구현했다
'''

import sys

def floyd():
    for k in range(1, n+1): # 경유지를 나타낼 반복문
        for i in range(1, n+1): # 시작지를 나타낼 반복문
            for j in range(1, n+1): # 도착지를 나타낼 반복문
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j]) # 기존 시작-도착 경로와 k를 거쳐가는 경로를 비교해 작은 것을 선택

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

matrix = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)] # 플로이드 워셜은 인접행렬이 필요함
for i in range(1, n+1):
    matrix[i][i] = 0 # 자기 자신에게 가는 거리는 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a][b] = min(matrix[a][b], c) # 직접 어딘가에 도달할 수 있다면 그 최소값을 선택

floyd()

for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i][j] == sys.maxsize: print(0, end=" ")
        else: print(matrix[i][j], end=" ")
    print()