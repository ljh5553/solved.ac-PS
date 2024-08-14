import sys

N, M = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

sum = [0]
for i in range(len(li)):
    sum.append(sum[i] + li[i])

for _ in range(M):
    f, t = map(int, sys.stdin.readline().split())
    print(sum[t] - sum[f-1])