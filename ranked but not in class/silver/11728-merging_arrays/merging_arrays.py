'''
https://www.acmicpc.net/problem/11728 - 배열 합치기

소요시간 10분, 풀이성공

아이디어 : 포인터 2개를 이용해 작은 숫자부터 새 배열로 옮기기

시간복잡도 : O(N+M)

자료구조 : 

느낀점 : 머지소트와 유사한 느낌으로 접근해 투포인터로 해결했다
         사실 리스트의 extend와 sort 메소드로 풀면 훨씬 코드가 간결했지만
         문제의 의도는 그게 아닐 것이기 때문에 투포인터로 접근함
'''

import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

merged = []
aptr, bptr = 0, 0

while aptr < N and bptr < M:
    if A[aptr] <= B[bptr]:
        merged.append(A[aptr])
        aptr += 1
    
    else:
        merged.append(B[bptr])
        bptr += 1

if aptr >= N:
    while bptr < M:
        merged.append(B[bptr])
        bptr += 1

else:
    while aptr < N:
        merged.append(A[aptr])
        aptr += 1

print(*merged)