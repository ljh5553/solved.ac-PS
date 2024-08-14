import sys

li = []
N = int(sys.stdin.readline())
for _ in range(N):
    a, n = map(str, sys.stdin.readline().split())
    a = int(a)
    li.append([a, n])
    
li.sort(key = lambda x: (x[0]))
for item in li:
    print(item[0], item[1])