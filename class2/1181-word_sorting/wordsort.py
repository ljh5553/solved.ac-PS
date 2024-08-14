import sys

ws = []
N = int(sys.stdin.readline())
for _ in range(N):
    w = sys.stdin.readline().strip()
    ws.append(w)

ws = list(set(ws))
ws.sort()
ws.sort(key=len)

for i in ws:
    print(i)