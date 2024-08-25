'''
https://www.acmicpc.net/problem/9663 - N-Queen

소요시간 X분, 풀이X, 유튜브 영상으로 처음 구현해봄

아이디어 : 같은 폴더의 nqueens.py 폴더 참조

시간복잡도 : 

자료구조 : 

느낀점 : 과거 알고리즘 강의에서 구현하는 방법대로 구현한건데 파이썬은 느려서 통과가 안 되는듯
         아마 C, C++, 자바같은 다른 언어를 활용하면 가능하다고 보여짐
'''

import sys
sys.setrecursionlimit(10**6)

def ispromising(d):
    for i in range(d):
        if row[i] == row[d] or abs(row[d] - row[i]) == abs(d - i): return False
    return True

def nqueens(depth):
    global cnt

    if depth == N:
        cnt += 1
        return
    
    else:
        for i in range(N):
            row[depth] = i
            if ispromising(depth):
                nqueens(depth+1)

N = int(sys.stdin.readline())
row = [0 for _ in range(N)]
cnt = 0
nqueens(0)
print(cnt)