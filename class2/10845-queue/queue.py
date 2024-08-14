import sys

N = int(input())
q = []
front = -1
back = -1
for _ in range(N):
    c = sys.stdin.readline().split()
    
    if c[0] == "push":
        if front == -1: front += 1
        back += 1
        q.insert(back, c[1])
    elif c[0] == "pop":
        if front == -1 and back == -1: print("-1")
        else:
            print(q[front])
            front += 1
            if front > back: front, back = -1, -1
    elif c[0] == "size":
        if front == -1 and back == -1: print("0")
        else: print(back-front+1)
    elif c[0] == "empty":
        if front == -1 and back == -1: print("1")
        else: print("0")
    elif c[0] == "front":
        if front == -1 and back == -1: print("-1")
        else: print(q[front])
    elif c[0] == "back":
        if front == -1 and back == -1: print("-1")
        else: print(q[back])