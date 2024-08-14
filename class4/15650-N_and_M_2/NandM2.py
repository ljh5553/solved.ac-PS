'''
아이디어 : 백트래킹. 1부터 시작해서 순열 조건을 만족하는 것만 정답 리스트에 넣기

시간복잡도 : N!, N=8

자료구조 : 정답저장용 리스트, 방문저장용 리스트
'''

import sys

def bt(depth):
    if depth == M:
        print(*ans)
        return
    
    for i in range(1, N+1):
        if visited[i] == 0:
            if not ans or ans[depth-1] < i:
                visited[i] = 1
                ans.append(i)
                bt(depth+1)
                visited[i] = 0
                ans.pop()

N, M = map(int, sys.stdin.readline().split())

ans = []
visited = [0 for _ in range(N+1)]

bt(0)