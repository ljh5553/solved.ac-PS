'''
아이디어 : 백트래킹. 1부터 M+1까지 반복문을 돌면서 비내림차순을 만족하면 정답리스트에 추가

시간복잡도 : N^N, N=8. 가능. 중복가능은 N^N, 8이하면가능이고 중복불가능은 N!, 10이하면가능

자료구조 : 정답저장용 리스트
'''

import sys

def bt(depth):
    if depth == M:
        print(*ans)
        return
    
    for i in range(1, N+1):
        if not ans or ans[depth-1] <= i:
            ans.append(i)
            bt(depth+1)
            ans.pop()

N, M = map(int, sys.stdin.readline().split())

ans = []
bt(0)