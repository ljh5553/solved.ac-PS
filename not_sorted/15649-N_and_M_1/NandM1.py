'''
아이디어 : 백트래킹 순열찾기. for문으로 N만큼 반복 후 depth가 M이 되면 재귀 종료

시간복잡도 : N!, N <= 8 이므로 가능. 10이하면 가능함

자료구조 : 순열저장용 리스트, 방문확인용 리스트
'''

import sys

def bt(depth):
    if depth == M:
        print(*ans)
        return

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            ans.append(i)
            bt(depth+1)
            visited[i] = 0
            ans.pop()

N, M = map(int, sys.stdin.readline().split())

ans = []
visited = [0 for _ in range(N+1)]

bt(0)