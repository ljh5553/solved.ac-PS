'''
https://www.acmicpc.net/problem/1182 - 부분수열의 합

소요시간 20분, 풀이성공

아이디어 : 백트래킹. 부분수열을 원소 1개, 2개 ... 으로 만들어가면서 합의 값이 S가 되는 부분수열이면 카운트를 늘림
           만약 백트래킹의 깊이가 원소의 개수까지 도달했을 경우 부분수열이 아니므로 리턴 <- 사실 아니었음
           모든 원소를 포함한 것도 부분수열의 일부이다

시간복잡도 : O(N!)

자료구조 : 주어진 수열 저장용 리스트, 방문확인용 리스트, 경우의 수 카운터

느낀점 : 부분수열이라길래 자기 자신은 포함 안 되는줄 알았더니 자기자신도 포함이었다

         다른 사람의 코드를 보니 백트래킹 함수 인자에 지금까지 원소의 합을 넣어서
         현재 값을 더하지 않은 것과 현재 값을 더한 것 두 가지 케이스로 재귀를 2번 호출함
'''

import sys
sys.setrecursionlimit(10**6)

def bt(depth, idx):
    global cnt

    if depth == N+1: return

    if sum(ans) == S and depth != 0:
        cnt += 1
    
    for i in range(idx, len(nums)):
        if visited[i] == False:
            ans.append(nums[i])
            visited[i] = True
            bt(depth+1, i+1)
            ans.pop()
            visited[i] = False

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

ans = []
visited = [False for _ in range(N)]
cnt = 0
bt(0, 0)
print(cnt)