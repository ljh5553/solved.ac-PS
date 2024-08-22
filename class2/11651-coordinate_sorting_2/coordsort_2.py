'''
https://www.acmicpc.net/problem/11651 - 좌표 정렬하기 2

소요시간 4분, 풀이성공, 정답구글링 X

아이디어 : 람다식을 이용해 2가지 기준으로 정렬, 첫번째 : y좌표 오름차순 / 두번째 : x촤표 오름차순

시간복잡도 : O(N log N)

자료구조 : 좌표저장용 리스트

느낀점 : 간단한 문제여서 바로 해결함. 정렬 메소드의 key 인자를 람다식으로 쓰는걸 복습할 수 있었다
'''

import sys

N = int(sys.stdin.readline())
c = list()
for _ in range(N):
    c.append(list(map(int, sys.stdin.readline().split())))

c.sort(key = lambda x : (x[1], x[0]))

for item in c:
    print(item[0], item[1])