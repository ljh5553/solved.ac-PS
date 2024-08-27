'''
https://www.acmicpc.net/problem/15683 - 감시

소요시간 X분, 풀이X, 유튜브 강의영상 시청 후 구현

아이디어 : CCTV의 가능한 모든 방향에 따라 브루트포스로 경우의 수를 따져봄
           4진법을 이용해 각 CCTV의 방향을 확인함. CCTV가 3개 있고 0-북, 1-동, 2-남, 3-서 로 가정
           4진법 013은 1번 CCTV가 북쪽, 2번 CCTV가 동쪽, 3번 CCTV가 서쪽을 보고 있다는 의미임

           각 CCTV의 종류에 따라 방향은 정해져있으므로 (2번은 0,2 또는 1,3 / 3번은 0,1,2 또는 1,2,3... 과 같이)
           방향에 따라서 그 부분을 쭉 따라 벽이 있는지 체크하면서 나아가면 됨

시간복잡도 : (4 * 8 * 8 + 64) * 4**CCTV개수
              ^^^^^   ^   ^^    ^^^^^^^^^^^
     surv 호출수      | 빈칸확인연산량    ㄴ방향의 개수 ** CCTV의 개수
                surv의 연산량
              
자료구조 : 지도저장용 2차원리스트, 경우의 수 따져볼 때마다 갱신할 결과지도 2차원리스트

느낀점 : 방향이나 특정 색 등을 표현할 때는 그 경우의 수에 맞는 진법을 이용하는 아이디어가 포인트
'''

import sys

def is_outside(a, b):
    if 0 <= a < N and 0 <= b < M: return False
    return True

def surv(r, c, d):
    d %= 4

    while True:
        r += dr[d]
        c += dc[d]

        if is_outside(r, c) or rst[r][c] == 6: return
        if rst[r][c] != 0: continue
        rst[r][c] = -1

N, M = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cctvs = []
rst = [[0 for _ in range(M)] for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0 and matrix[i][j] != 6: cctvs.append((i, j))
        if matrix[i][j] == 0: ans += 1

for temp in range(4 ** len(cctvs)):

    for i in range(N):
        for j in range(M):
            rst[i][j] = matrix[i][j]
    
    brute = temp

    for i in range(len(cctvs)):
        di = brute % 4
        brute = brute // 4

        cr, cc = cctvs[i]

        if matrix[cr][cc] == 1:
            surv(cr, cc , di)
        
        elif matrix[cr][cc] == 2:
            surv(cr, cc , di)
            surv(cr, cc , di+2)

        elif matrix[cr][cc] == 3:
            surv(cr, cc , di)
            surv(cr, cc , di+1)

        elif matrix[cr][cc] == 4:
            surv(cr, cc , di)
            surv(cr, cc , di+1)
            surv(cr, cc , di+2)

        else:
            surv(cr, cc , di)
            surv(cr, cc , di+1)
            surv(cr, cc , di+2)
            surv(cr, cc , di+3)
    
    val = 0
    for i in range(N):
        for j in range(M):
            if rst[i][j] == 0: val += 1
    ans = min(ans, val)

print(ans)