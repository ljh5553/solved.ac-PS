'''
https://www.acmicpc.net/problem/16928 - 뱀과 사다리 게임

소요시간 30분초과, 풀이실패, 구글링해서 풀었음

아이디어 : BFS, 각 노드에서는 앞으로 1~6칸 가는 경우가 있고 도착한 지점에 사다리나 뱀이 있을 경우 도착지점으로 값을 바꿔줌

시간복잡도 : O(V log E), V = 100 E = 6

자료구조 : BFS를 위한 큐

느낀점 : 아이디어도 빠르게 생각해서 20분만에 구현했는데 결국 틀렸다
         일단 오타를 내서 u, v 를 넣어야하는 부분에 x, y를 넣는 실수를 했음
         
         또한 사다리를 포함해 엣지를 다 그래프에 그리는게 아니라 1부터 6까지의 주사위 숫자는 고정이니
         반복문을 1~6까지 돌려서 그 자리에 사다리나 뱀이 있는지 확인하면 됨
         또한 큐 안에 튜플형태로 카운터를 넣으면 메모리 초과가 발생하므로 꼭 리스트를 사용해야함

         다른 사람들은 사다리와 뱀을 저장할 때 딕셔너리를 썼는데 나는 리스트를 썼다
         어차피 값 하나만 저장할건데 굳이 딕셔너리를 쓸 이유도 없고
         오히려 in 키워드를 사용해 O(N)의 시간으로 있는지 없는지 검사하는 것보다는
         리스트를 이용해 목적지 값만 바로 가져와 유효한 값이면 있는거고 0이면 없다고 보는데 더 빠를 것 같음
'''

import sys
from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        v = q.popleft()

        if v == 100: return cnt[v]

        for k in range(1, 7):
            i = v + k

            if i > 100: continue
            if visited[i] == 1: continue

            if ladders[i] != 0:
                i = ladders[i]
            
            if snakes[i] != 0:
                i = snakes[i]
            
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                cnt[i] = cnt[v] + 1
                

ladders = [0 for _ in range(101)]
snakes = [0 for _ in range(101)]

N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    ladders[x] = y
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    snakes[u] = v

visited = [0 for _ in range(101)]
cnt = [0 for _ in range(101)]
print(bfs(1))