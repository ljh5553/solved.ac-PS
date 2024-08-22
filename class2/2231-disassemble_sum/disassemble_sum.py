'''
https://www.acmicpc.net/problem/2231 - 분해합

아이디어 : 브루트포스로 분해합을 계속 찾아내기

시간복잡도 : O(N*7) 7000000 < 1억

자료구조 : 
'''

import sys

def sol(n):
    for i in range(1, n):
        ans = 0
        origin = i

        while i != 0:
            ans += i % 10
            i = i // 10
        ans += origin

        if ans == n: return origin
    
    return 0

N = int(sys.stdin.readline())
print(sol(N))
