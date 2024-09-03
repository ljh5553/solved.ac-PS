'''
https://www.acmicpc.net/problem/1874 - 스택 수열

소요시간 22분, 풀이성공

아이디어 : 주어진 숫자보다 적게 넣었다면 일단 주어진 숫자까지 스택에 넣고 상황를 저장하며
           주어진 숫자와 현재까지 넣은 숫자를 비교해 주어진 숫자까지 스택에서 빼고 상황을 저장한다
           이 때 스택에서 빼는 숫자가 현재 숫자가 아니라면 불가능한 경우이므로 반복문을 탈출해 NO를 출력한다

           이 부분이 다른 사람보다 비효율적인 부분이었는데, 어차피 pop을 해서 수열을 만드는 것이므로
           꺼낸 숫자를 현재 숫자까지 while문으로 처리하지 않고 단순히 pop만 해서 비교하면 된다

시간복잡도 : 

자료구조 : 스택을 구현할 리스트

느낀점 : 문제를 보고 바로 이해하고 풀었는데 제대로 생각하지 않고 일단 구현부터 해서 생각보다 애먹었다
         단순히 쉬워보인다고 막 시작하지 말고 풀이를 제대로 생각한 뒤 시작해야겠다
'''

import sys

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

s = []
cnt = 1
ans = []
flag = 0

for i in range(n):
    if nums[i] >= cnt:
        while cnt <= nums[i]:
            s.append(cnt)
            ans.append("+")
            cnt += 1
    
    temp = nums[i]
    if nums[i] <= cnt:
        while temp >= nums[i]: # while이 필요없고 단순히 nums[i]와 s[-1]을 비교해 같으면 -연산, 다르면 break하면 된다
            a = s.pop()

            if a != nums[i]:
                flag = 1
                break

            ans.append("-")
            temp -= 1

    if flag == 1: break

if flag == 1: print("NO")
else:
    for item in ans:
        print(item)