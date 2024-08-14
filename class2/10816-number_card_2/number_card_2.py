import sys

N = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))

C_dict = {}
for item in C:
    if not C_dict.get(item): C_dict[item] = 1
    else: C_dict[item] += 1

for item in T:
    if C_dict.get(item): print(C_dict[item], end=" ")
    else: print("0", end=" ")