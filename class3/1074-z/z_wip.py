# 시간초과

import sys

def sol(N, m, x, y):   
    if N == 1:
        dx = [0, 0, 1, 1]
        dy = [0, 1, 0, 1]

        for i in range(4):
            global cnt
            m[x + dx[i]][y + dy[i]] += cnt
            cnt += 1

    else:
        sol(N-1, m, x, y)
        sol(N-1, m, x, y + (2**N)//2)
        sol(N-1, m, x + (2**N)//2, y)
        sol(N-1, m, x + (2**N)//2, y + (2**N)//2)

N, r, c = map(int, sys.stdin.readline().split())
m = [[0 for _ in range(2**N)] for _ in range(2**N)]
cnt = 0

sol(N, m, 0, 0)
print(m[r][c])