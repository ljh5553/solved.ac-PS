'''
https://www.acmicpc.net/problem/4673 - 셀프 넘버

소요시간 9분, 풀이성공

아이디어 : 1부터 10000까지 셀프넘버인지 아닌지 판단하는 테이블을 만든 뒤
           1부터 10000까지 각 숫자별로 d(n)을 생성해 그 숫자를 인덱스로 테이블에 False로 바꿔준다
           어떤 숫자로 d(n)이 만들어진다는 것은 그 d(n)으로 만든 숫자가 셀프넘버가 될 수 없다는 뜻이므로
           10000까지 체크해본 뒤 True만 골라 출력하면 된다

시간복잡도 : 10000*5

자료구조 : 셀프넘버 여부를 저장할 테이블

느낀점 : 모듈러연산과 테이블 아이디어만 있다면 쉽게 풀 수 있는 문제였다
'''

sn = [True for _ in range(10001)]
for i in range(1, 10001):
    n = 0
    temp = i

    while temp != 0:
        n += temp % 10
        temp = temp // 10
    
    if i + n <= 10000:
        sn[i+n] = False

for i in range(1, 10001):
    if sn[i] == True: print(i)