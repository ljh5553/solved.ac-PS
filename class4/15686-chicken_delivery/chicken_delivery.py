'''
https://www.acmicpc.net/problem/15686 - 치킨 배달

소요시간 28분, 풀이성공, 시뮬레이션 문제라는 것을 알고 풀었음

아이디어 : 시뮬레이션. 치킨집을 M개 선택한 뒤 그 치킨집에 대해 각 집까지의 맨해튼거리를 연산해 최소값을 구함

시간복잡도 : 13을 M개의 조합으로 만드는 최고값(1716정도?) * 100 * 13

자료구조 : 

느낀점 : itertools의 combinations를 이용해 조합을 구한 뒤 풀었음
         치킨집에서 각 집까지의 거리를 어떻게 구하나 고민했는데 반대로 생각해봐서
         각 집에서 모든 치킨집 거리의 최소값을 구했고 이것이 들어맞았음
'''

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

chickens = []
houses = []
ans = 10000

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1: houses.append((i, j))
        if matrix[i][j] == 2: chickens.append((i, j))

for sel in combinations(chickens, M):
    s = 0
    for h in houses:
        mn = 10000
        for c in sel:
            a, b = h
            x, y = c
            dist = abs(a-x) + abs(b-y)
            mn = min(mn, dist)
        s += mn
    ans = min(ans, s)

print(ans)