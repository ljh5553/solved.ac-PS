'''
https://www.acmicpc.net/problem/2292 - 벌집

소요시간 18분, 풀이성공

아이디어 : 0 6 18 36 과 같이 6*n 씩 증가하므로 목표 숫자를 넘을 때까지 카운터를 증가시키며 곱해줌

시간복잡도 : 

자료구조 : 

느낀점 : 처음엔 들어온 숫자에 나누기를 반복해 0을 만들고 카운트를 하려고 했으나 6*n 중 n을 알아야했으므로
         직관적으로 떠오른 풀이대로 0부터 곱해가면서 풀기로 방향을 바꾸었다
         처음 떠오른 풀이가 있다면 그걸 그대로 구현하는 방식이 더 좋을듯
'''

import sys

n = int(sys.stdin.readline())
n = n - 1
cnt = 0
temp = 0

while temp < n:
    cnt += 1
    temp = temp + (6 * cnt)

print(cnt+1)