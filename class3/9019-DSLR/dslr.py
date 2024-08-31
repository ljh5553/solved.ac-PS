'''
https://www.acmicpc.net/problem/9019 - DSLR

소요시간 30분초과, 풀이실패, 풀이 구글링 참고

아이디어 : BFS를 이용해 각 연산마다 하나씩 탐색

시간복잡도 : O(V + E), V = 10000 E = 4 ?

자료구조 : BFS구현을 위한 큐

느낀점 : 접근방식은 다 맞았는데 구현에서 L와 R 연산을 deque의 rotate 메소드를 사용하니 시간초과가 났다
         L과 R연산은 수학적으로 접근해서 한 번에 연산하면 코드의 길이도 간결하고 시간도 빠름
         물론 이렇게 해도 pypy3로 제출해야 통과한다
'''

import sys
from collections import deque

def dslr(n):
    q = deque([(n, "")])
    visited[n] = 1

    while q:
        v, op = q.popleft()

        if v == B:
            print(op)
            return

        d = v * 2 % 10000
        if visited[d] == 0:
            q.append((d, op+"D"))
            visited[d] = 1
        
        s = (v-1) % 10000
        if visited[s] == 0:
            q.append((s, op+"S"))
            visited[s] = 1
        
        l = (v % 1000) * 10 + (v // 1000)
        if visited[l] == 0:
            q.append((l, op+"L"))
            visited[l] = 1

        r = (v // 10) + (v % 10) * 1000
        if visited[r] == 0:
            q.append((r, op+"R"))
            visited[r] = 1

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    visited = [0 for _ in range(10000)]
    dslr(A)