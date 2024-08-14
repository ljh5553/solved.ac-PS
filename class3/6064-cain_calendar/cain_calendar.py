'''
아이디어 : 숫자쌍이 일종의 최소공배수

시간복잡도 : n? 

자료구조 : 

느낀점 : 최소공배수 포인트를 잡아야함. 유클리드 호제법 이용
'''

import sys

def gcd(a, b):
    if a % b == 0: return b
    return gcd(b, a % b)

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    year_max = (M * N) / gcd(M, N)
    ans = x

    while ans <= year_max:
        if (ans - 1) % N + 1 == y: break
        ans += M
    
    if ans > year_max: print("-1")
    else: print(ans)