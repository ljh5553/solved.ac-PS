'''
https://www.acmicpc.net/problem/15683 - 감시

소요시간 180분 초과, 풀이실패, 시도 이후 유튜브 강의영상 시청

아이디어 : cctv의 각 4방향에 대해서 각각 감시할 수 있는 타일을 조사한 뒤
           5번부터 1번까지 최대로 감시할 수 있는 경우를 선택해서 감시함

시간복잡도 : 

자료구조 : 

느낀점 : 무조건 5 4 3 2 1 순서대로 하면 테스트케이스에 나와있지 않은 반례에서 틀리게 된다
         예시 : 1 0 0 0 0 0     1 0 0 0 1
                0 2 0 0 0 0     0 1 0 1 0
                0 0 3 0 0 0     0 0 0 0 0
                0 0 0 4 0 0     0 1 0 1 0
                0 0 0 0 5 0     1 0 0 0 1
                0 0 0 0 0 6
                ans : 4         ans : 1
'''

import sys
from collections import defaultdict

def calc_cctv(num):
    crs = list()
    ccs = list()
    for item in cctvs[num]:
        cr, cc = item[0], item[1]
        crs.append(cr)
        ccs.append(cc)
    
    return crs, ccs

def apply_surv(req, r, c):
    for item in req:
        if item == 0:
                for i in range(r-1, -1, -1):
                    if matrix[i][c] == 6: break
                    if matrix[i][c] == 0: matrix[i][c] = -1
        if item == 1:
                for i in range(c+1, M):
                    if matrix[r][i] == 6: break
                    if matrix[r][i] == 0: matrix[r][i] = -1
        if item == 2:
                for i in range(r+1, N):
                    if matrix[i][c] == 6: break
                    if matrix[i][c] == 0: matrix[i][c] = -1
        if item == 3:
                for i in range(c-1, -1, -1):
                    if matrix[r][i] == 6: break
                    if matrix[r][i] == 0: matrix[r][i] = -1

def count_4way(r, c):
    cnt = [0 for _ in range(4)]

    for i in range(r-1, -1, -1):
        if matrix[i][c] == 6: break
        if matrix[i][c] == 0: cnt[0] += 1
        
    for i in range(c+1, M):
        if matrix[r][i] == 6: break
        if matrix[r][i] == 0: cnt[1] += 1
    
    for i in range(r+1, N):
        if matrix[i][c] == 6: break
        if matrix[i][c] == 0: cnt[2] += 1

    for i in range(c-1, -1, -1):
        if matrix[r][i] == 6: break
        if matrix[r][i] == 0: cnt[3] += 1

    return cnt

def find_max(rst):
    max, max_idx = -1, -1
    for i in range(len(rst)):
        if max < rst[i]:
            max = rst[i]
            max_idx = i
    return max, max_idx
    
N, M = map(int, sys.stdin.readline().split())
matrix = list()
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

cctvs = defaultdict(list)

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1: cctvs[1].append((i, j))
        if matrix[i][j] == 2: cctvs[2].append((i, j))
        if matrix[i][j] == 3: cctvs[3].append((i, j))
        if matrix[i][j] == 4: cctvs[4].append((i, j))
        if matrix[i][j] == 5: cctvs[5].append((i, j))

if cctvs[5]:
    c5rs, c5cs = calc_cctv(5)
    
    for i in range(len(c5rs)):
        r, c = c5rs[i], c5cs[i]
        cnt = count_4way(r, c)
        rst = [sum(cnt)]
        max, max_idx = find_max(rst)
        apply_surv([0, 1, 2, 3], r, c)

if cctvs[4]:
    c4rs, c4cs = calc_cctv(4)

    for i in range(len(c4rs)):
        r, c = c4rs[i], c4cs[i]

        cnt = count_4way(r, c)
        
        rst = list()
        for i in range(4):
            rst.append(cnt[i] + cnt[(i+1)%4] + cnt[(i+2)%4])

        max, max_idx = find_max(rst)

        if max_idx == 0: apply_surv([0, 1, 2], r, c)
        if max_idx == 1: apply_surv([1, 2, 3], r, c)
        if max_idx == 2: apply_surv([2, 3, 0], r, c)
        if max_idx == 3: apply_surv([3, 0, 1], r, c)

if cctvs[3]:
    c3rs, c3cs = calc_cctv(3)

    for i in range(len(c3rs)):
        r, c = c3rs[i], c3cs[i]
        cnt = count_4way(r, c)
        
        rst = list()
        for i in range(4):
            rst.append(cnt[i] + cnt[(i+1)%4])
        
        max, max_idx = find_max(rst)

        if max_idx == 0: apply_surv([0, 1], r, c)
        if max_idx == 1: apply_surv([1, 2], r, c)
        if max_idx == 2: apply_surv([2, 3], r, c)
        if max_idx == 3: apply_surv([3, 0], r, c)

if cctvs[2]:
    c2rs, c2cs = calc_cctv(2)

    for i in range(len(c2rs)):
        r, c = c2rs[i], c2cs[i]
        cnt = cnt = count_4way(r, c)
        
        rst = list()
        for i in range(2):
            rst.append(cnt[i] + cnt[i+2])
        
        max, max_idx = find_max(rst)

        if max_idx == 0: apply_surv([0, 2], r, c)
        else: apply_surv([1, 3], r, c)

if cctvs[1]:
    c1rs, c1cs = calc_cctv(1)

    for i in range(len(c1rs)):
        r, c = c1rs[i], c1cs[i]
        cnt = count_4way(r, c)
        max, max_idx = find_max(cnt)

        if max_idx == 0: apply_surv([0], r, c)
        if max_idx == 1: apply_surv([1], r, c)
        if max_idx == 2: apply_surv([2], r, c)
        if max_idx == 3: apply_surv([3], r, c)

ans = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0: ans += 1
print(ans)