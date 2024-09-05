'''
https://www.acmicpc.net/problem/1316 - 그룹 단어 체커

소요시간 8분, 풀이성공

아이디어 : 앞의 알파벳과 비교해 다른 알파벳이라면 빈도수를 보고,
           처음 나온 알파벳이면 빈도수를 올리고 이미 나온 알파벳이면 그룹단어가 아니므로 break한다
           앞과 같은 알파벳이면 빈도수만 올린다

           for else 문으로 break되지 않았다면 그룹단어인 것이니 정답 카운트를 올려준다

시간복잡도 : 

자료구조 : 빈도수 체크용 딕셔너리

느낀점 : 딕셔너리를 활용해 빈도수를 체크한다는 아이디어만 생각할 수 있으면 간단하게 해결할 수 있다
'''

import sys
from collections import defaultdict

ans = 0
N = int(sys.stdin.readline())
for _ in range(N):
    word = sys.stdin.readline().strip()
    freq = defaultdict(int)
    freq[word[0]] = 1

    for i in range(1, len(word)):
        if word[i] != word[i-1]:
            if freq[word[i]] == 0:
                freq[word[i]] += 1
            else:
                break
        else:
            freq[word[i]] += 1
    else: ans += 1
        
print(ans)