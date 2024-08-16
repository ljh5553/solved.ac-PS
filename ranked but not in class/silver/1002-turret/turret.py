'''
아이디어 : 원의 방정식을 이용한 외접,내접 구하기

시간복잡도 :

자료구조 :
'''

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)

    if d == 0:
        if r1 == r2: print(-1)
        else: print(0)
    else:
        if (r1 + r2) ** 2 == d or abs((r2 - r1) ** 2) == d: print(1)
        elif abs((r2 - r1) ** 2) < d < (r1 + r2) ** 2: print(2)
        else: print(0)