'''
https://www.acmicpc.net/problem/1929 - 소수 구하기

소요시간 9분, 풀이성공, 정답구글링 X

아이디어 : 에라토스테네스의 체를 이용해 특정 구간에 있는 소수 구하기

시간복잡도 : O(n log log n) <- 에라토스테네스의 체 시간복잡도

자료구조 : 소수인지 아닌지 판단하는 정보를 저장할 리스트

느낀점 : 에라토스테네스의 체를 복습할 수 있었음
         다른 사람들의 코드를 보니 배열 대신 set을 사용하는 것을 볼 수 있었음. 직관적으로 set에서 숫자들을 제거함
'''

import sys

M, N = map(int, sys.stdin.readline().split())

prime = [True for i in range(N+1)]
prime[0], prime[1] = False, False

for i in range(2, int(N**(1/2))+1):
    if prime[i] == True:
        j = 2
        while i * j < N+1:
            prime[i*j] = False
            j += 1

for i in range(M, N+1):
    if prime[i] == True: print(i)