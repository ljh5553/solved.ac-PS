'''
아이디어 : heapq 모듈로 최소 힙 구현
           단 최대힙을 구성할 때처럼 튜플로 만들어 첫 번째 값을 절댓값으로 놓고 pop할 때 1번인덱스 값을 받아옴

시간복잡도 : O(log N)

자료구조 : 최소힙
'''

import sys, heapq

hq = []
N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(hq) == 0: print(0)
        else: print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (abs(x), x))