'''
아이디어 : 최대 100*100의 2차원배열을 만들고 직사각형이 있는 범위에 1 마킹, 이후 1의 개수 카운팅

시간복잡도 : 2중for O(N^2). N은 최대 100, 즉 10000 < 2억

자료구조 : 문제에 주어진 x y x y 좌표계를 저장할 리스트, 좌표계를 나타낼 2차원리스트
'''

import sys

square_coord = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
coord = [[0 for _ in range(101)] for _ in range(101)]
for k in range(4):
    x1, y1, x2, y2 = square_coord[k]
    y1, y2 = abs(y1 - 100), abs(y2 - 100)
    for i in range(y2, y1):
        for j in range(x1, x2):
            if coord[i][j] == 0:
                coord[i][j] = 1

cnt = 0
for i in range(0, 101):
    for j in range(0, 101):
        if coord[i][j] == 1: cnt += 1

print(cnt)