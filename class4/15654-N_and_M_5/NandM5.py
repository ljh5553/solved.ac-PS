'''
아이디어 : 백트래킹. 숫자 리스트를 정렬한 후 작은 숫자부터 하나씩 골라가며 백트래킹 시행

시간복잡도 : N!, N<=8

자료구조 : 숫자저장용 리스트, 방문저장용 리스트, 정답저장용 리스트
'''

import sys

def bt(depth):
    if depth == M:
        print(*ans)
        return

    for i in range(len(nums)):
        if visited[i] == 0:
            if nums[i] not in ans:
                ans.append(nums[i])
                visited[i] = 1
                bt(depth + 1)
                ans.pop()
                visited[i] = 0

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
ans = []
visited = [0 for _ in range(N)]
bt(0)