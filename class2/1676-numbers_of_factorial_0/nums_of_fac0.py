'''
https://www.acmicpc.net/problem/1676 - 팩토리얼 0의 개수

소요시간 10분, 풀이성공, 정답구글링X

아이디어 : 팩토리얼을 구한 후 문자열로 만들어 처음 0이 나올 때까지 발견된 숫자 개수 구하기

시간복잡도 : 

자료구조 : 

느낀점 : 처음엔 재귀함수로 팩토리얼을 계산했는데 메모리초과, 이후 math 라이브러리로 계산했더니 통과
         사실은 수학문제로, 2*5를 할 때 0이 늘어나는 점에서 착안해 5의 개수를 구하는 것이였음
'''

import sys, math

N = int(sys.stdin.readline())

# 첫 번째 방법, math 라이브러리로 팩토리얼 계산 후 단순히 세기
f = math.factorial(N)
fs = str(f)
cnt, idx = 0, -1

while True:
    if fs[idx] != "0": break
    if idx < -1 * len(fs): break

    cnt += 1
    idx -= 1

# 두 번째 방법, 2*5 하는 순간 5를 캐치해 5의 개수를 계산하기
cnt_2 = 0
while(N > 1):
    cnt_2 += N // 5
    N = N // 5

print(cnt)
print(cnt_2)