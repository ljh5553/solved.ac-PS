'''
아이디어 : - 를 기준으로 분리한 뒤 다시 + 기준으로 분리해 값을 더해준 다음 더한 값들을 서로 빼면 됨

시간복잡도 : ?

자료구조 : 입력저장용 스트링변수, 각 더하기 결과 저장용 리스트
'''

import sys

T = sys.stdin.readline().strip()

nums = []
split_m = T.split("-")
for item in split_m:
    total = 0
    split_p = item.split("+")
    for n in split_p:
        total += int(n)
    nums.append(total)

ans = nums[0]
for i in range(1, len(nums)):
    ans -= nums[i]
print(ans)