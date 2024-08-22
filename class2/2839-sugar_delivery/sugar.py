'''
https://www.acmicpc.net/problem/2839 - 설탕 배달

소요시간 23분, 풀이성공, 정답구글링 X

아이디어 : 그리디. 먼저 5kg 봉지로 채울 수 있을 만큼 채우고 3kg 봉지 채우기
           불가능하면 3kg 봉지로 채울 수 있을 만큼 채우고 이거도안되면 -1 리턴

다른 사람의 아이디어 : 내가 생각한 접근법이 맞긴 한데, 다른 사람들은 5로 나누어떨어지면 몫 리턴
                       안 나누어떨어지면 3을 빼고 개수를 1 증가시킨다음 다시 5로 나누기를 시도하는 것을 반복함
                       결론적으로 11의 경우 11 -> 8 -> 5 -> 0 의 순서를 거쳐 3개라는 답이 나옴

시간복잡도 : O(N) ??

자료구조 : 

느낀점 : 나누어 떨어진다는 것을 잘 생각해서 몫과 모듈러연산을 잘 활용해야함
'''

import sys

N = int(sys.stdin.readline())
flag = 0

if N < 3: print(-1)

if N >= 5:
    
    cnt, kg = 0, N

    for i in range((N // 5), 0, -1):
        kg = N - i*5
        if kg % 3 == 0:
            cnt = i + (kg // 3)
            kg %= 3
            break
    
    if kg == 0: print(cnt)
    else: flag = 1

if 3 <= N < 5 or flag == 1:
    if N % 3 != 0: print(-1)
    else: print(N // 3)