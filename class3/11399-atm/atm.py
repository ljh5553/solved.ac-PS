import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P.sort()
for i in range(N-1):
    P[i+1] = P[i] + P[i+1]
print(sum(P))