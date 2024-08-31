'''
https://www.acmicpc.net/problem/10773 - 제로

소요시간 4분, 풀이성공

아이디어 : 스택에 수를 차례대로 입력하고 0이 들어왔을 경우 pop을 해준 뒤 sum한다

시간복잡도 : O(1)?

자료구조 : 스택을 구현할 리스트

느낀점 : 기초적인 스택 활용이었음
'''

import sys

s = []
K = int(sys.stdin.readline())
for _ in range(K):
    n = int(sys.stdin.readline())
    if n == 0: s.pop()
    else: s.append(n)
print(sum(s))