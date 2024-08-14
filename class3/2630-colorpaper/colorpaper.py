import sys

def sol(m, start_x, start_y, l):
    c = m[start_x][start_y]
    global w, b

    for i in range(start_x, start_x + l):
        for j in range(start_y, start_y + l):
            if c != m[i][j]:
                sol(m, start_x, start_y, l // 2)
                sol(m, start_x, start_y + l // 2, l // 2)
                sol(m, start_x + l // 2, start_y, l // 2)
                sol(m, start_x + l // 2, start_y + l // 2, l // 2)
                return

    if c == 0: w += 1
    elif c == 1: b += 1

N = int(sys.stdin.readline())
m = []
for _ in range(N):
    m.append(list(map(int, sys.stdin.readline().split())))

w, b = 0, 0
sol(m, 0, 0, N)
print(w)
print(b)