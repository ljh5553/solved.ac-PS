'''
아이디어 : 지수법칙, 나머지분배법칙을 이용한 수학적 분할정복 풀이

시간복잡도 : log N. N = 2147483647

자료구조 : 단순연산이므로 딱히없음
'''

import sys

def sol(a, b, c):
    if b == 1: return a % c
    
    if b % 2 == 0:
        return (sol(a, b//2, c) ** 2) % c
    else:
        return ((sol(a, b//2, c) ** 2) * a) % c
    
a, b, c = map(int, sys.stdin.readline().split())
print(sol(a, b, c))