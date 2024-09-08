'''
https://www.acmicpc.net/problem/1406 - 에디터

소요시간 30분초과, 풀이실패

아이디어 : 구현. 스택 2개를 이용해 커서방향으로 pop하도록 붙여놓은 후 ( 스택1-> 커서 <-스택2 )
           L일 때는 왼쪽 스택에서 빼서 오른쪽 스택에 넣고, D일 때는 오른쪽 스택에서 빼서 왼쪽 스택에 넣는다
           이렇게 하면 커서를 따로 구현할 필요 없이 스택 사이가 기준점이 되어서 자동으로 작동하게 됨

           B일 때는 단순히 왼쪽 스택에서 하나를 뺀 뒤 버리면 되고 P일 때도 왼쪽 스택에 하나를 붙여주면 된다

           출력을 할 때는 오른쪽 스택이 반전되어 있으므로 왼쪽 스택과 오른쪽 스택을 반대로 돌린 것을 붙여준 뒤
           형식에 맞춰 출력하면 됨

시간복잡도 : O(1)

자료구조 : 스택을 구현할 리스트

느낀점 : 커서는 인덱스를 가리키는 포인터로, 삭제는 포인터-1의 문자를 0으로 치환하고 포인터를 왼쪽으로 한 칸 옮기는 것으로 구현했는데
         추가는 나머지 문자들을 다 밀어야 해서 분명 시간 초과가 날 것이라고 생각해 시도하지 않았다
'''

import sys

s1 = list(sys.stdin.readline().strip())
s2 = []
m = int(sys.stdin.readline())

for _ in range(m):
    cmd = list(map(str, sys.stdin.readline().split()))

    if cmd[0] == "L" and s1:
        s2.append(s1.pop())

    elif cmd[0] == "D" and s2:
        s1.append(s2.pop())

    elif cmd[0] == "B" and s1:
        s1.pop()

    elif cmd[0] == "P":
        s1.append(cmd[1])

ans = s1+s2[::-1]
print("".join(ans))