'''
https://www.acmicpc.net/problem/4949 - 균형잡힌 세상

소요시간 12분, 풀이성공

아이디어 : 스택을 이용해 왼쪽괄호가 있으면 스택에 넣고 오른쪽괄호가 있으면 스택에 넣은 뒤 peak과 비교해 같으면 pop 2번
           이후 스택에 무언가 남아있으면 no 출력, 비어있으면 yes 출력

시간복잡도 : 

자료구조 : 스택을 구현할 리스트

느낀점 : 간단한 문제처럼 보여도 리스트의 길이를 벗어나는 예외처리를 잘 해야한다
'''

import sys

stack = []
while True:
    s = sys.stdin.readline().rstrip()
    if s == ".": break

    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[":
            stack.append(s[i])
        
        if s[i] ==")":
            stack.append(s[i])
            if len(stack) > 1 and stack[-2] == "(":
                stack.pop()
                stack.pop()

        if s[i] == "]":
            stack.append(s[i])
            if len(stack) > 1 and stack[-2] == "[":
                    stack.pop()
                    stack.pop()
    
    if stack: print("no")
    else: print("yes")
    stack.clear()