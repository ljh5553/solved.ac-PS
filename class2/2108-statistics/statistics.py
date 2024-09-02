'''
https://www.acmicpc.net/problem/2108 - 통계학

소요시간 21분, 풀이성공

아이디어 : 산술평균은 단순히 sum과 나누기를 이용, round 내장함수를 직접 만들었다가 모듈 내장 함수로 바꿈
           중앙값은 리스트를 정렬한 뒤 N을 2로 나눈 몫의 위치에 있는 값을 출력
           최빈값은 딕셔너리를 이용해 빈도수를 구한 뒤 가장 많이 나오는 것들을 리스트에 저장한 후
           리스트의 길이가 1이면 1개만 있는거니 그대로 출력, 2 이상이라면 정렬해서 2번째 값을 출력
           범위는 중앙값에 사용된 정렬된 리스트에서 맨 앞과 맨 뒤의 값의 차이를 출력

시간복잡도 : 

자료구조 : 

느낀점 : 간단한 문제였지만 round함수가 골치아프게 만들었다
         또한 딕셔너리의 keys values items 메소드를 더 잘 활용할 수 있어야겠다
'''

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
li = []
for _ in range(N):
    li.append(int(sys.stdin.readline()))

print(round(sum(li)/N))

li_sorted = sorted(li)
print(li_sorted[N//2])

freq = defaultdict(int)
for item in li:
    freq[item] += 1

mx = max(freq.values())
p = []
for k, v in freq.items():
    if v == mx:
        p.append(k)
p.sort()
if len(p) == 1: print(p[0])
else: print(p[1])

print(li_sorted[-1] - li_sorted[0])