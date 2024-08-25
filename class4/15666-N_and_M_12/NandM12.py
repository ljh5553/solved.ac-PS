'''
https://www.acmicpc.net/problem/15666 - N과 M (12)

소요시간 16분, 풀이성공, 풀이구글링 X

아이디어 : 백트래킹 순열찾기
           각 depth마다 비내림차순 여부를 검사해 가능하면 넣고 다음 depth로 불가능하면 다른 숫자로 시도

시간복잡도 : O(N^N)

자료구조 : 순열저장용 리스트, 주어진 숫자 저장용 리스트

느낀점 : 다른 사람들의 풀이를 보니 입력을 set으로 받아서 중복을 제거하거나
         for item in nums 대신 for i in range(depth, N) 을 활용해 비내림차순인지 따로 검사를 안 하고도
         자동으로 비내림차순으로 만드는 아이디어가 있었음
         (이미 받고 sort를 했기 때문에 이전 인덱스의 값은 무조건 같거나 작음
         그러므로 depth부터 살펴보면 무조건 같거나 큰 숫자만 있다)
         
'''

import sys
sys.setrecursionlimit(10**6)

def bt(depth):
    last = -1

    if depth == M:
        print(*ans)
        return
    
    for item in nums:
        if not ans or ans[depth-1] <= item:
            if last == item: continue
            ans.append(item)
            bt(depth+1)
            ans.pop()
            last = item

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
visited = []
ans = []
bt(0)