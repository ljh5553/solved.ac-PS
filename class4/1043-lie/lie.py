'''
https://www.acmicpc.net/problem/1043 - 거짓말

소요시간 X분, 풀이실패, 구글링 해답 찾기 후 구현

아이디어 : 분리 집합. 처음 진실을 알고 있는 사람의 집합을 만든 뒤 각 파티마다 교집합을 찾아
           교집합이 공집합이 아니라면 그 파티에선 진실을 말해야 하므로 진실 집합에 추가
           교집합이 공집합이라면 진실을 알고 있는 사람이 없으므로 패스
           이렇게 진실 집합을 모두 구하고 다시 모든 파티에 대해 진실을 알고 있는 사람과 교집합을 찾아
           공집합인 파티만 숫자를 세면 됨

시간복잡도 : 

자료구조 : 진실을 알고 있는 사람의 집합(set)

느낀점 : 진실을 알고 있는 사람과 거짓을 알고 있는 사람을 연결해서 BFS를 한다는
         아이디어를 세웠고 아이디어 자체는 맞았는데 구현에 어려움을 겪었다

         지금까지 집합 문제는 거의 없어서 set을 사용하는 방법조차 잊어버렸는데
         set의 메소드를 다시 한 번 확인하는 시간이었다
'''

import sys

N, M = map(int, sys.stdin.readline().split())
truth = set(sys.stdin.readline().split()[1:])

parties = []
for _ in range(M):
    parties.append(set(sys.stdin.readline().split()[1:]))

for _ in range(M):
    for p in parties: # 모든 파티에 대해 처리해야 최종 결과를 알 수 있음
        if p & truth: # 파티에 있는 사람과 진실을 알고 있는 사람의 교집합이 있다면
            truth = truth.union(p) # 파티에 있는 사람을 진실을 알고 있는 사람으로 추가

ans = 0
for p in parties:
    if p & truth: continue # 이 파티에선 진실을 말해야하므로 세지 않음
    ans += 1

print(ans)