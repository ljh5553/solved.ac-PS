'''
아이디어 : DP. 두 번째 행부터 바로 위 행의 같은 열 값을 제외하고 다른 두 값의 최소값을 더해줌

시간복잡도 : N

자료구조 : dp저장용 2차원리스트
'''

import sys

N = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N):
    costs[i][0] = costs[i][0] + min(costs[i-1][1], costs[i-1][2])
    costs[i][1] = costs[i][1] + min(costs[i-1][0], costs[i-1][2])
    costs[i][2] = costs[i][2] + min(costs[i-1][0], costs[i-1][1])

print(min(costs[-1]))