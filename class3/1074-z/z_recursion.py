'''
https://www.acmicpc.net/problem/1074 - Z

소요시간 X분, 풀이X, 유튜브 영상으로 처음 구현해봄

아이디어 : 재귀함수를 이용
           현재 주어진 r과 c가 각 사각형의 부분 중 어느 부분에 속하는지 판정 후
           그 사각형의 가장 상단 왼쪽의 값과 다시 재귀적으로 사각형을 쪼개 함수를 호출하고 더함
           가장 상단 왼쪽의 값은 현재 사각형 크기를 절반한 값을 제곱의 값에 각각 1 2 3 4 를 곱함

           최종적으로 더 이상 사각형을 쪼갤 수 없다면 0을 리턴하는 base condition을 가짐

시간복잡도 : 

자료구조 : 

느낀점 : 기존 풀이는 대충 구글링으로 재귀 안 쓰는 해결법을 찾아서 했는데 정석적인 풀이는 이 방법인듯
'''

import sys
sys.setrecursionlimit(10**6)

def sol(r, c, n):
    if n == 0: return 0

    half = (2**n)//2
    if r < half and c < half: return sol(r, c, n-1)
    elif r < half and c >= half: return (half**2) + sol(r, c-half, n-1)
    elif r >= half and c < half: return 2*(half**2) + sol(r-half, c, n-1)
    elif r >= half and c >= half: return 3*(half**2) + sol(r-half, c-half, n-1)

N, r, c = map(int, sys.stdin.readline().split())
print(sol(r, c, N))