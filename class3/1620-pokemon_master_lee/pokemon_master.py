'''
아이디어 : 해시맵을 사용해 들어오는 값을 저장하고 찾음

시간복잡도 : 충돌이 없을 때 해시테이블 탐색 O(1)

자료구조 : 번호와 인덱스를 저장할 딕셔너리

느낀점 : 해시테이블을 만들어놓고 그 안에서 또 반복문으로 탐색하지 말고 하나의 테이블에 다 때려박으면 됨
'''

import sys

N, M = map(int, sys.stdin.readline().split())

pokemon = dict()

for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    pokemon[i] = name
    pokemon[name] = i

for _ in range(M):
    q = sys.stdin.readline().strip()
    
    if q.isdigit(): print(pokemon[int(q)])
    else: print(pokemon[q])