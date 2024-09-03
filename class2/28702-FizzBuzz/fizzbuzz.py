'''
https://www.acmicpc.net/problem/28702 - FizzBuzz

소요시간 36분, 풀이실패

아이디어 : 3부터 1까지 반복하는 반복문에서 입력을 읽으며 숫자인 경우 현재 상수를 더하고 빠져나온다
           즉 빠져나온 상수는 들어온 입력 다음에 올 숫자고 이를 배수인지 판단해서 알맞은 출력만 하면 됨

시간복잡도 : 

자료구조 : 

느낀점 : 그냥 단순히 처음으로 보는 숫자를 찾아 다음 숫자를 유추한 뒤 배수인지만 판단하는 문제였는데
         너무 복잡하게 생각해서 못 풀었다
'''

import sys

for i in range(3, 0, -1):
    a = sys.stdin.readline().strip()
    if a not in ["Fizz", "Buzz", "FizzBuzz"]:
        n = int(a) + i
        break

if n % 15 == 0: print("FizzBuzz")
elif n % 5 == 0: print("Buzz")
elif n % 3 == 0: print("Fizz")
else: print(n)