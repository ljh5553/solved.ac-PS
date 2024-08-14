import sys

N, M = map(int, sys.stdin.readline().split())

set_N = set()
set_M = set()

for _ in range(N):
    set_N.add(sys.stdin.readline().strip())
for _ in range(M):
    set_M.add(sys.stdin.readline().strip())

deutbojab = set_N & set_M
print(len(deutbojab))
deutbojab_li = list(deutbojab)
deutbojab_li.sort()
for item in deutbojab_li:
    print(item)