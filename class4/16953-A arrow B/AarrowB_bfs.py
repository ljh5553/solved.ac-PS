'''
https://www.acmicpc.net/problem/16953 - A → B

소요시간 9분, 풀이성공, 풀이 구글링 참고함

아이디어 : 숨바꼭질 BFS 문제와 유사하게 BFS로 가능한 경로를 탐색해서 목표에 도달하는 최소경로를 찾음

시간복잡도 : O(V log E)
              
자료구조 : BFS용 큐

느낀점 : 오랜만에 풀어보는 BFS라 좀 당황한 부분이 있었음
         특히 메모리 초과를 안 내려고 visited 리스트를 선언해야 고민했는데
         큐에 카운터를 넣음으로서 해결함
'''

import sys
from collections import deque

def bfs(start):
    q = deque([(start, 1)])

    while q:
        v, c = q.popleft()

        if v > B: continue
        if v == B:
            print(c)
            return
        for i in (v*2, v*10+1):
            q.append((i, c+1))
    
    print(-1)

A, B = map(int, sys.stdin.readline().split())
bfs(A)