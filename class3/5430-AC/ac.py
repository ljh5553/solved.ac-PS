'''
https://www.acmicpc.net/problem/5430 - AC

소요시간 40분, 풀이성공, 덱과 덱에 포함된 reverse 메소드는 못 쓴다는 힌트를 얻고 투포인터로 진행

아이디어 : 각 테스트케이스에 대해 리스트는 인덱싱과 split()으로 나눠 리스트에 저장하고
           명령어도 인덱싱으로 어떤 문자인지 파악해서 연산 실행

           위가 첫 번째로 떠오른 아이디어였는데 reverse() 메소드는 O(N)만큼의 연산이 들어가
           결국 시간초과로 실패했다

           이후 질문게시판에서 투포인터라는 힌트를 얻어 덱의 첫 번째와 마지막 요소에 각각 포인터를 두고
           R이 들어오면 작동할 커서를 바꿔주고 D가 들어오면 진행방향으로 포인터를 이동시킨 뒤
           모든 작업이 끝나면 작동할 커서의 방향으로 요소를 출력시킴

시간복잡도 : 

자료구조 : 들어오는 숫자를 저장할 덱

느낀점 : 시간복잡도를 고려하지 않고 처음엔 단순히 덱과 reverse를 쓰면 되겠다고 생각했는데
         훨씬 더 빠른 방법이 있었다
'''

import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    cmd = sys.stdin.readline().strip()
    size = int(sys.stdin.readline())
    data = sys.stdin.readline().strip()

    data = data[1:len(data)-1]

    if not data:
        deq = deque([])
    else:
        deq = deque(map(int, data.split(",")))

    lptr, rptr = 0, len(deq)-1
    focus = 0 # 0 for lptr, 1 for rptr

    iserror = False
    for i in range(len(cmd)):
        if cmd[i] == "R":
            if focus == 0: focus = 1
            else: focus = 0
        if cmd[i] == "D":
            if lptr > rptr or rptr < lptr:
                iserror = True
                print("error")
                break

            if focus == 0:
                lptr += 1
            else:
                rptr -= 1

    if not iserror:
        if focus == 0:
            print("[", end="")
            for i in range(lptr, rptr+1):
                if i == rptr:
                    print(deq[i], end="")
                    break
                print(deq[i], end=",")
            print("]")
        else:
            print("[", end="")
            for i in range(rptr, lptr-1, -1):
                if i == lptr:
                    print(deq[i], end="")
                    break
                print(deq[i], end=",")
            print("]")