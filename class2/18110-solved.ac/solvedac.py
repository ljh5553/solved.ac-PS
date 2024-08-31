'''
https://www.acmicpc.net/problem/18110 - solved.ac

소요시간 10분, 풀이성공

아이디어 : 리스트로 값을 저장한 뒤 정렬하고 덱으로 옮겨 앞과 뒤에서 pop을 해주고 평균값을 냄

시간복잡도 : 

자료구조 : 자료저장용 리스트, pop용 덱

느낀점 : 0으로 나누는 예외처리를 해줘야한다
         파이썬의 round() 내장함수는 반올림을 처리해주지만
         x.5에 대해서 x가 짝수면 내림하고 홀수면 올림을 하는 사사오입 원칙을 적용한다
         이 이상한 점 때문에 직접 int()를 이용해 반올림 함수를 구현함
'''

import sys
from collections import deque

def round(n):
    if n - int(n) >= 0.5: return int(n)+1
    else: return int(n)

n = int(sys.stdin.readline())
li = []

for i in range(n):
    a = int(sys.stdin.readline())
    li.append(a)

li.sort()
nr = round(n*0.15)
dq = deque(li)

for _ in range(nr):
    dq.popleft()
    dq.pop()

if len(dq) == 0: print(0)
else: print(round(sum(dq)/len(dq)))