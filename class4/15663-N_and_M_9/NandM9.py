'''
아이디어 : 백트래킹. 주어진 수열을 정렬 -> 첫 요소부터 백트래킹 시행. 최대길이면 출력, 최대길이가 아니면 방문검사와 마지막 재귀에서 나온 숫자가 아닐 시 백트래킹

시간복잡도 : N!, N <= 8

자료구조 : 정답저장 리스트, 방문저장 리스트, 마지막 재귀함수에 대한 숫자 저장 변수
'''

import sys

def bt(depth):
    if depth == M:
        print(*ans)
        return
    
    last_num = -1
    for i in range(len(nums)):
        if visited[i] == 0 and nums[i] != last_num:
            visited[i] = 1
            ans.append(nums[i])
            last_num = nums[i]
            bt(depth+1)
            ans.pop()
            visited[i] = 0

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

ans = []
visited = [0 for _ in range(N)]
last_num = -1
nums.sort()
bt(0)