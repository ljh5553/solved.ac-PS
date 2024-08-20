'''
아이디어 : 해시테이블을 이용해 키-사이트주소, 밸류-비밀번호로 저장, 주소를 받아서 결과값 반환

시간복잡도 : O(1)

자료구조 : 딕셔너리
'''

import sys

N, M = map(int, sys.stdin.readline().split())

pwdict = dict()
for _ in range(N):
    site, pw = map(str, sys.stdin.readline().split())
    pwdict[site] = pw

for _ in range(M):
    print(pwdict[sys.stdin.readline().strip()])