import sys

board = []
M, N = map(int, sys.stdin.readline().split())
for _ in range(M):
    board.append(sys.stdin.readline().strip())

cnt = []
for i in range(M-7):
    for j in range(N-7):
        cnt_w, cnt_b = 0, 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if board[k][l] != "W": cnt_w += 1
                    else: cnt_b += 1
                else:
                    if board[k][l] != "B": cnt_w += 1
                    else: cnt_b += 1
        cnt.append(min(cnt_w, cnt_b))

print(min(cnt))