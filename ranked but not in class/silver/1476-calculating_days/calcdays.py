'''
https://www.acmicpc.net/problem/1476 - 날짜 계산

소요시간 28분, 풀이성공

아이디어 : 브루트포스, 주어진 E S M 값에 맞도록 계속 더하고 조건을 벗어나면 맞게 수정해주면서 최종 답을 찾음

시간복잡도 : 

자료구조 : 

느낀점 : 대충 문제를 보고 GCD를 이용하는 카잉달력(6064)과 비슷하다고 생각했지만 하나씩 계산해보며 푸는 브루트포스 문제였다
'''

import sys

E, S, M = map(int, sys.stdin.readline().split())

e, s, m = 1, 1, 1
ans = 1
while True:   
    if (e - 1) % 15 == 0: e = 1
    if (s - 1) % 28 == 0: s = 1
    if (m - 1) % 19 == 0: m = 1

    if e == E and s == S and m == M:
        print(ans)
        break

    ans += 1
    e += 1
    s += 1
    m += 1