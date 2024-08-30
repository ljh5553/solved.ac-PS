'''
https://www.acmicpc.net/problem/7662 - 이중 우선순위 큐

소요시간 27분, 풀이실패, 구글링 후 구현

아이디어 : 최소힙과 최대힙 2개를 만들어 최소값을 빼야하면 최소힙의 피크를, 최대값을 뺴야하면 최대힙의 피크를 제거

시간복잡도 : k log N ??

자료구조 : 최대힙, 최소힙, 방문확인용 리스트

느낀점 : 최소힙 최대힙을 따로 만든다는 아이디어는 맞았는데 힙을 동기화시키는 과정에서 시간초과가 발생
         최소값을 뺄 때 최소힙에서 pop 할 때 1, 최대힙에서 remove 할 때 N, 최대힙을 다시 heapify 할 때 N 이라 2N+1으로
         어떻게 넘어갈 줄 알았는데 생각해보니 k번 반복이라 k*N으로 리스트에 100개만 집어넣어도 1억번임

         힙에 튜플의 형태로 ID를 부여해서 리스트에 방문여부를 기록하고 삽입 명령이 들어오면 튜플로 값과 ID를 묶어서 푸쉬,
         제거 명령이 들어오면 최소값일 때 최소힙의 피크 ID를 방문리스트에, 최대값일 때 최대힙의 피크 ID를 방문리스트에 기록한 뒤
         while문을 돌려 최대힙 최소힙에 대해 각각 힙 안에 값이 있고 첫 번째 값이 방문리스트에 기록되어있으면
         하나씩 팝을 해주면 자동으로 방문처리가 된 요소들은 팝이 되면서 최종적으로는 동기화가 된다
'''

import sys
from heapq import heappush, heappop

T = int(sys.stdin.readline())
for _ in range(T):
    maxh = []
    minh = []

    k = int(sys.stdin.readline())
    visited = [0 for _ in range(k)]

    for i in range(k):
        cmd = list(map(str, sys.stdin.readline().split()))
        op, n = cmd[0], int(cmd[1])

        if op == "I":
            heappush(minh, (n, i))
            heappush(maxh, (-n, i))
        else:
            if n == -1:
                if minh: visited[heappop(minh)[1]] = 1
            else:
                if maxh: visited[heappop(maxh)[1]] = 1

        while minh and visited[minh[0][1]] == 1:
            heappop(minh)
        while maxh and visited[maxh[0][1]] == 1:
            heappop(maxh)
    
    if not minh: print("EMPTY")
    else: print(-maxh[0][0], minh[0][0])
