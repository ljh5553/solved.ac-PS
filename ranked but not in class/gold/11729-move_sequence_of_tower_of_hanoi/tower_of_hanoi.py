'''
https://www.acmicpc.net/problem/11729 - 하노이 탑 이동 순서

소요시간 X분, 풀이X, 유튜브 영상으로 처음 구현해봄

아이디어 : 재귀함수를 이용
           1번에서 3번으로 k개의 원판을 이동하려면 k-1개의 원판을 2번으로 이동시킨 뒤
           1번에 남은 k번째 원판을 3번으로 이동시키고 2번에 들어간 남은 것들을
           3번으로 이동시켜주면 됨

           즉, 첫 번째 재귀함수로는 1번에서 2번으로 k-1개를 이동하고 하나만 있는 것이 아니라면
           재귀적인 사고를 통해 base condition까지 문제를 쪼갬
           base condition은 n == 1 일 때, 단순히 하나만 있으므로 a번에서 b번으로 이동시키기만 하고
           이후로 다시 돌아가서 나머지 것들을 움직여주면 됨

시간복잡도 : 

자료구조 : 

느낀점 : 재귀적인 사고를 통해 k번째 행동이 가능하다면 k+1번째 행동도 k-1을 통해 해결할 수 있다는
         것을 보여야 하는데 어려움.
         재귀함수의 인자가 하나만 있는 것이 아니라, a b n 과 같이 출발지 목적지까지 명시한]
         여러 개일 수도 있음
'''

import sys
sys.setrecursionlimit(10**6)

def sol(a, b, n):
    global cnt

    if n == 1:
        ans.append([a, b])
        cnt += 1
        return

    sol(a, 6-a-b, n-1)
    ans.append([a, b])
    cnt += 1
    sol(6-a-b, b, n-1)

N = int(sys.stdin.readline())
cnt = 0
ans = []
sol(1, 3, N)
print(cnt)
for item in ans:
    print(item[0], item[1])