import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))

A_d = {}

for item in A:
    A_d[item] = 1

for item in T:
    if A_d.get(item): print("1")
    else: print("0")