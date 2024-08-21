'''
https://www.acmicpc.net/problem/30804 - 과일 탕후루

아이디어 : 투포인터 문제. 과일 나열의 맨 앞에 왼쪽 및 오른쪽 포인터를 배치한 후
           오른쪽 포인터를 한 칸씩 우측이동시키며 과일의 개수를 셈
           이 때 과일 개수가 3이상이 될 때, 왼쪽 포인터 칸의 과일을 제거하고 왼쪽 포인터를 우측이동함
           이를 과일 개수가 2개이하가 될 때까지 반복해 개수를 2개로 유지시킴
           이 때 지금까지의 길이 최대값을 저장

           오른쪽 포인터가 전체 과일 나열을 초과하면 종료

시간복잡도 :

자료구조 : 과일 나열을 저장할 리스트, 과일 개수를 저장할 딕셔너리, 왼쪽 및 오른쪽 포인터
'''

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

fruits = defaultdict(int)
num_fruits = 0
l, r = 0, 0
ans = -1

while r < N:
    if fruits[seq[r]] == 0: num_fruits += 1
    fruits[seq[r]] += 1

    while num_fruits > 2:
        fruits[seq[l]] -= 1
        if fruits[seq[l]] == 0: num_fruits -= 1
        l += 1
    
    ans = max(ans, r-l+1)
    r += 1

print(ans)