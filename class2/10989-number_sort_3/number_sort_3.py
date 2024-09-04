'''
https://www.acmicpc.net/problem/10989 - 수 정렬하기 3

소요시간 12분, 풀이성공

아이디어 : 딕셔너리로 숫자의 빈도수를 계산한 뒤 키값으로 정렬하고 딕셔너리에서 값을 하나씩 빼고 밸류만큼 반복한다

시간복잡도 : 2N + N log N

자료구조 : 

느낀점 : 처음에는 N이 10000000이고 정렬이 N log N이기에 시간초과가 걸릴 것 같았지만 제한이 5초여서 단순히 정렬해서 출력했다
         그 결과 메모리초과로 틀렸다. 8MB제한인데 시간복잡도에 집중한 나머지 놓쳐버린 것

         그래서 공간을 줄이려면 어떻게 해야하나 생각했는데 딕셔너리를 이용해 키는 숫자 밸류는 빈도수로 계산해
         나온 빈도수 만큼 반복출력하면 되겠다고 생각했다

         이 과정에서 딕셔너리 정렬법을 몰랐기 때문에 검색으로 해결했다.
         딕셔너리에서 아이템을 뺀 뒤 sorted함수로 정렬하면 키값을 기준으로 정렬된다
         결과의 포맷은 리스트 안에 키와 밸류가 튜플 형태로 들어있고 dict()로 감싸주면 다시 딕셔너리가 된다

         밸류를 기준으로 정렬하는 법은 람다식을 사용해 배열의 두 번째 요소로 정렬하는 것 처럼 하면 된다.
         즉 sorted_dict = dict(sorted(original_dict.items(), key=lambda x : x[1]) 형태이다.

         내림차순 정렬을 원하면 다시 sorted 함수의 인자로 reverse=True 를 넣으면 된다
'''

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
nums = defaultdict(int)
for _ in range(N):
    a = int(sys.stdin.readline())
    nums[a] += 1

s = sorted(nums.items())
for k, v in s:
    for _ in range(v):
        print(k)