import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))
rst = 0
coins.sort(reverse=True)

for c in coins:
    if K >= c:
        rst += K // c
        K %= c

        if K <= 0: break
    
print(rst)