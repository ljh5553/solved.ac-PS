'''
https://www.acmicpc.net/problem/1966 - 프린터 큐

소요시간 37분, 풀이성공

아이디어 : 큐에서 최대값이 맨 앞에 올 때까지 전부 pop->append하고 최소값은 pop하며 카운트

시간복잡도 : 

자료구조 : 큐

느낀점 : 구현 자체는 빠르게 했는데 최대값이 큐의 맨 앞에 올 때까지 갱신하는 과정에서
         모듈러 연산을 q의 길이만큼이 아니라 N만큼 해서 idx의 값이 이상해지는 경우가 있었다
         이런 초보적인 실수를 더 줄여야할듯
'''

import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    docs = list(map(int, sys.stdin.readline().split()))
    
    q = deque(docs)
    t = docs[M]
    idx = M
    ans = 0

    while True:
        mx = max(q)
        while q[0] != mx:
            q.append(q.popleft())
            idx = (idx-1) % len(q)
        if idx == 0 and mx == t:
            ans += 1
            break
        else:
            q.popleft()
            ans += 1
            idx -= 1
    
    print(ans)