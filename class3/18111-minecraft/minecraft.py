'''
아이디어 : 가능한 땅의 높이인 0부터 256까지 모든 경우의 수에 대해 블럭 제거 및 놓기 계산
           만약 제거한 블럭 + 가지고있는 블럭보다 놓아야 할 블럭 수가 많다면 불가능한 경우이므로 컨티뉴
           가능하다면 기존 값과 시간을 비교한 뒤 같거나 작다면 그 높이 저장

시간복잡도 : 

자료구조 : 땅 지도 2차원리스트
'''

import sys

N, M, B = map(int, sys.stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

min_time = sys.maxsize
min_height = -1
for h in range(257):
    place_b = 0
    dig_b = 0
    for r in range(N):
        for c in range(M):
            if matrix[r][c] < h: place_b += h - matrix[r][c]
            else: dig_b += matrix[r][c] - h
    
    if dig_b + B < place_b: continue

    if dig_b * 2 + place_b <= min_time:
        min_time = dig_b * 2 + place_b
        min_height = h

print(min_time, min_height)