'''
https://www.acmicpc.net/problem/16953 - A → B

소요시간 35분, 풀이실패, 풀이 구글링 참고

아이디어 : top-down 방식으로 B에서 A를 만드는 경우를 탐색함
           뒤에 1을 붙이는 것이 더 빠르게 만드는 방법이므로 %10==1 이 참이면 10으로 몫을 구하고
           %10==1이 거짓이지만 %2==0이 참이면 2로 나눈다
           연산이 불가능한 경우면 방법이 없는 경우이므로 -1 출력
           연산이 완료되어 A==B가 되면 경우의 수를 모두 계산했으므로 카운터 출력

시간복잡도 : 
              
자료구조 : 

느낀점 : 처음엔 이전에 비슷한 문제를 DP로 풀었길래 bottom-up DP로 풀이를 시도했으나 메모리 초과가 남
         입력이 10**9 까지 들어올 수 있는데 bottom-up으로 풀면 메모리 초과가 뜸

         종이에 풀 때 top-down 방식으로 풀었는데 DP풀이는 bottom-up 방식에 너무 익숙해져있어서
         결국 bottom-up을 고집하다가 틀림. 직관적으로 풀어낸 방법을 코드화시켜보자

         while-else, for-else 문을 처음 접해봤는데 반복문 내에서 break되면 else를 실행시키지 않고
         break가 되지 않은 상태로 끝나면 else문을 실행시키는 구문임
'''

import sys
A, B = map(int, sys.stdin.readline().split())

cnt = 1
while B != A:
    cnt += 1
    temp = B

    if B % 10 == 1: B = B // 10
    elif B % 2 == 0: B = B // 2
    
    if B == temp:
        print(-1)
        break

else: print(cnt)