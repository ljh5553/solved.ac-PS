'''
https://www.acmicpc.net/problem/9663 - N-Queen

소요시간 X분, 풀이X, 유튜브 영상으로 처음 구현해봄

아이디어 : 백트래킹. 한 자리에 놓으면 같은 행, 열 및 대각선에 못 놓기에
           지점별로 놓을 수 있는지 검사한 뒤 가능하다면 진행하고 불가능하면 뒤로 돌아감

           코드에서 depth는 행을 뜻하고 i 는 열을 뜻함
           visited_linear 리스트는 i 번째 열에 놓을 수 없으면 True, 놓을 수 있으면 False
           visited_rightup은 오른쪽 대각선 위로 올라가는 선을 그어서 그 부분에 놓을 수 없으면 True, 놓을 수 있으면 False
           visited_leftdown은 왼쪽 대각선 아래로 올라가는 선을 그어서 그 부분에 놓을 수 없으면 True, 놓을 수 있으면 False

           각 리스트들에 대해서 O(1)의 시간에 놓을 수 있는지를 검사한 뒤 가능하면 다음 행으로 백트래킹을 진행하고
           불가능하다면 진행하지 않고 다음 열에 놓을 수 있는지 검사

           마지막 열에 도달하면 가능한 경우가 있다는 뜻이므로 카운트를 증가시키고 리턴해서 다음 경우의 수를 탐색함

시간복잡도 : O(N!)

자료구조 : 어떤 열, 오른쪽위 대각선, 왼쪽아래 대각선 상에서 놓을 수 있는지 기록하는 리스트 3개

느낀점 : 이 코드가 파이썬으로 통과가 가능한 이유는 리스트로 O(1)의 시간에 가능한지 불가능한지를 판단하기 때문
         
'''

import sys
sys.setrecursionlimit(10**6)

def bt(depth):
    global cnt

    if depth == N:
        cnt += 1
        return
    
    for i in range(N):
        if visited_linear[i] or visited_rightup[i + depth] or visited_leftdown[i - depth + N - 1]: continue

        visited_linear[i], visited_rightup[i + depth], visited_leftdown[i - depth + N - 1] = True, True, True
        bt(depth+1)
        visited_linear[i], visited_rightup[i + depth], visited_leftdown[i - depth + N - 1] = False, False, False

N = int(sys.stdin.readline())
cnt = 0
visited_linear = [False for _ in range(N)]
visited_rightup = [False for _ in range(N*2)]
visited_leftdown = [False for _ in range(N*2)]
bt(0)
print(cnt)