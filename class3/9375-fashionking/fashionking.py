'''
아이디어 : 해시테이블에 각 분류별 의상을 저장한 뒤 조합 찾기
           조합은 (a종류수 + 1) * (b종류수 + 1) * ... * (n종류수 + 1) - 1
           어떤 종류의 옷을 하나 고르거나 또는 안 고르거나 하는 경우의 수를 모두 곱한 뒤 아무 것도 안 입은 경우를 하나 빼줌

시간복잡도 : N^N?

자료구조 : 의상저장 딕셔너리
'''

import sys
from collections import defaultdict

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    clothes = defaultdict(list)
    for _ in range(N):
        c, t = map(str, sys.stdin.readline().split())
        clothes[t].append(c)
    
    comb = 1
    for item in clothes:
        comb *= len(clothes[item]) + 1

    print(comb-1)