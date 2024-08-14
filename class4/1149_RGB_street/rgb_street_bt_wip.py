'''
아이디어 : 백트래킹. 이전 노드의 색이 아니면 진행

시간복잡도 : X

자료구조 : 각 집의 비용 2차원리스트, 각 iteration의 비용합 리스트
'''

import sys

def bt(depth, cost, lastcolor):
    if depth == N:
        totals.append(cost)
        return
    
    for i in range(3):
        if lastcolor != i:
            lastcolor = i
            cost += paintcosts[depth][i]
            bt(depth+1, cost, lastcolor)
            cost -= paintcosts[depth][i]

N = int(sys.stdin.readline())
paintcosts = []
for _ in range(N):
    paintcosts.append(list(map(int, sys.stdin.readline().split())))

totals = []
bt(0, 0, -1)
print(min(totals))