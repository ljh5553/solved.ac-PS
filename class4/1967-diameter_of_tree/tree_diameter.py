'''
https://www.acmicpc.net/problem/1967 - 트리의 지름

소요시간 30분초과, 풀이실패

아이디어 : dfs를 2회 실행함. 첫 번째 bfs는 루트노드에서 가장 먼 리프노드를 찾아간 뒤 그 노드값을 저장하고
           두 번째 bfs에서는 가장 먼 리프노드에서 가장 먼 다른 노드(즉, 트리의 지름)을 찾음
           visited 배열은 -1로 초기화한 뒤 재귀적으로 거리값을 더해 저장한 거리의 배열로 활용해 메모리를 아낌

시간복잡도 : O(2 * (V + E)), V = 10000 E = 3

자료구조 : 방문확인용 리스트, 트리를 저장할 딕셔너리(양방향 그래프 구현)

느낀점 : 처음엔 모든 경로가 보장되니까 다익스트라를 통해 거리를 구한 뒤 최댓값을 출력하려고 했는데
         시간 초과가 나왔다
         리프 노드를 for문으로 구한 뒤 그 리프 노드에서 다익스트라를 하나씩 실행시켜 max값을 찾으니
         O(N) + O(N * V log E) + O(N) 으로 상당히 복잡해져서 그런 듯 하다

         다익스트라를 구현하다 코드를 까먹어서 이전에 풀었던 풀이를 참고했다. 까먹지 않게 자주 풀어야할듯ㄴ
'''

import sys

sys.setrecursionlimit(10**6)

def dfs(s, d): # s는 시작 노드값, d는 지금까지의 거리누적합
    visited[s] = d # 방문배열은 거리누적합을 저장

    for w, i in tree[s]:
        if visited[i] == -1:
            dfs(i, d+w)


n = int(sys.stdin.readline())
tree = dict()
for i in range(n+1):
    tree[i] = []
for _ in range(n-1):
    p, c, d = map(int, sys.stdin.readline().split())
    tree[p].append((d, c))
    tree[c].append((d, p))

leaves = []
for i in range(1, len(tree)):
    if len(tree[i]) == 1: leaves.append(i)

visited = [-1 for _ in range(n+1)]
dfs(1, 0) # 루트노드부터 dfs로 모든 다른 노드를 탐색

leaf = visited.index(max(visited)) # 가장 먼 리프노드의 번호를 저장
visited = [-1 for _ in range(n+1)]
dfs(leaf, 0) # 그 리프노드의 번호부터 다시 다른 모든 노드를 탐색

print(max(visited))