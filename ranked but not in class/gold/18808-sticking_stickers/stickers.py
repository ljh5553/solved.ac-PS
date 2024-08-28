'''
https://www.acmicpc.net/problem/18808 - 스티커 붙이기

소요시간 59분, 풀이성공, rotate함수에 쓰인 2차원리스트 회전은 구글링했음. 이후 유튜브 강의영상 시청

아이디어 : 모든 스티커에 대해 왼쪽 상단부터 붙일 수 있는지 검사 후 불가능하면 회전한 뒤 다시 검사

시간복잡도 : 4 * 40 * 40 * 10 * 10 * 100
             ^^^^^^^^^^^   ^^^^^^^   ^^^-- 최대 스티커의 개수
    각 모눈종이에 대해    모눈종이를 특정
    노트북에 놓을 수      위치에 놓을 수 있는지
    있는지 확인           확인하는 연산

자료구조 : 

느낀점 : 1시간 걸리고 약간 참고하긴 했어도 스스로 풀어서 정답을 받은 문제
         90도 회전의 규칙성을 찾다가 포기해서 구글링을 한 점이 아쉬움
'''

import sys

N, M, K = map(int, sys.stdin.readline().split())
stickers = []
for _ in range(K):
    R, C = map(int, sys.stdin.readline().split())
    temp = []
    for _ in range(R):
        temp.append(list(map(int, sys.stdin.readline().split())))
    stickers.append(temp)

matrix = [[0 for _ in range(M)] for _ in range(N)]

def stickable(sticker, a, b):
    for k in range(len(sticker)):
        for l in range(len(sticker[0])):
            if matrix[a+k][b+l] == 1 and sticker[k][l] == 1: return False
    return True

def stick(sticker, a, b):
    for k in range(len(sticker)):
        for l in range(len(sticker[0])):
            if matrix[a+k][b+l] == 0 and sticker[k][l] == 1: matrix[a+k][b+l] = 1

def rotate(sticker):
    new = [[0 for _ in range(len(sticker))] for _ in range(len(sticker[0]))]

    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            new[j][len(sticker)-i-1] = sticker[i][j]
    
    return new

for st in range(K):
    is_sticked = False
    
    for ang in range(4):
        for i in range(N-len(stickers[st])+1):
            for j in range(M-len(stickers[st][0])+1):
                if stickable(stickers[st], i, j):
                    stick(stickers[st], i, j)
                    is_sticked = True
                    break
            if is_sticked: break

        if is_sticked: break
        else: stickers[st] = rotate(stickers[st])

ans = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1: ans += 1
print(ans)