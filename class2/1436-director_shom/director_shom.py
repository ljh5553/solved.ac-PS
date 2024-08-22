'''
https://www.acmicpc.net/problem/1436 - 영화감독 숀

소요시간 23분, 풀이성공, 정답구글링 X

아이디어 : 브루트포스. 666부터 시작해서 숫자 자리수가 연속으로 6번이상 나오는 횟수를 세고, N번째 숫자면 리턴

시간복잡도 : O(?*5)

자료구조 : 

느낀점 : 찾는 반복문에서 브레이크를 제대로 안 해주면 무한루프에 빠진다. 여기서는 while 내부의 for문을 break하지 않아서 무한루프가 걸렸음
         다른 코드를 찾아보니 '666' in str 로 조건문대신 깔끔하게 작성함
'''

import sys

N = int(sys.stdin.readline())
num, find = 665, 0

while True:
    if find == N: break

    num_str = str(num)
    for i in range(-3, -1 * (len(num_str)+1), -1):
        if num_str[i] == "6" and num_str[i+1] == "6" and num_str[i+2] == "6":
            find += 1
            ans = num
            break
    num += 1

print(ans)