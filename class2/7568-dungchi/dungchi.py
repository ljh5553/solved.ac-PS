'''
https://www.acmicpc.net/problem/7568 - 덩치

소요시간 30분 초과, 풀이실패, 정답구글링 O

초기 아이디어 : (몸무게, 키) 순서대로 정렬 후 앞의 사람과 비교한 뒤 둘 다 작으면 등수가 낮아지고 둘 중 하나가 크면 등수 유지

실제 아이디어 : 2중 for문으로 모든 사람에 대해 각각 비교해본 후 등수 결정

시간복잡도 : O(N^2)

자료구조 : 사람저장용 리스트

느낀점 : 비교이기 때문에 2가지 기준으로 정렬하는건줄 알았음. 제한상 N이 50이하니까 브루트포스라는걸 짐작할 수 있었다
'''

import sys

N = int(sys.stdin.readline())
p = list()
for _ in range(N):
    p.append(list(map(int, sys.stdin.readline().split())))

for item in p:
    ranking = 1
    for comp in p:
        if comp[0] > item[0] and comp[1] > item[1]: ranking += 1
    print(ranking, end = " ")