'''
https://www.acmicpc.net/problem/15650 - N과 M (2)

소요시간 X분, 풀이X, itertools를 이용한 조합찾기를 구글링 후 구현

아이디어 : 

시간복잡도 : 

자료구조 : 

느낀점 : itertools에 포함된 combinations는 combinations(리스트, 뽑을숫자) 로 실행할 수 있는데
         리스트 내에서 뽑을숫자 개수만큼 사전순으로 조합을 만들어준다
         다만 하나의 오브젝트이므로 리스트처럼 직접 print할 수는 없고 iteration은 가능하기 때문에
         for ~ in combination(list, num) 같은 형태로 출력해야 한다
'''

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, N+1)]
for item in combinations(nums, M):
    print(*item)